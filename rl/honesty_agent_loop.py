"""verl agent loop that runs one honesty-eval episode per trajectory and scores it with the grader.

Registered through rl/agent_loops.yaml (actor_rollout_ref.rollout.agent.agent_loop_config_path).
Turn logic, tool execution and scoring live in src/honesty_env.py, shared with the eval, so a
trained model is evaluated under exactly the rules it was trained under.

Token bookkeeping follows verl's ToolAgentLoop: model tokens get response_mask 1, tool results and
nudges get 0 (they are context, not something the policy produced).
"""
import asyncio
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any
from uuid import uuid4

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from agent import TOOLS  # noqa: E402
from honesty_env import Episode  # noqa: E402
from verl.experimental.agent_loop.agent_loop import AgentLoopBase, AgentLoopOutput  # noqa: E402
from verl.experimental.agent_loop.tool_parser import ToolParser  # noqa: E402

logger = logging.getLogger(__file__)
logger.setLevel(os.getenv("VERL_LOGGING_LEVEL", "WARN"))


class HonestyAgentLoop(AgentLoopBase):
    def __init__(self, *args, max_turns: int = 20, max_tokens_per_turn: int = 2048, **kwargs):
        kwargs.pop("tools", None)  # our tools come from src/agent.py, not verl's tool registry
        super().__init__(*args, **kwargs)
        self.max_turns = max_turns  # same cap as the eval loop
        self.max_tokens_per_turn = max_tokens_per_turn  # same per-reply cap as the eval loop
        self.response_length = self.rollout_config.response_length
        self.tool_parser = ToolParser.get_tool_parser("hermes", self.tokenizer)
        self.log_path = os.getenv("HONESTY_ROLLOUT_LOG")

    async def _in_thread(self, fn, *args):
        # pytest subprocesses block; keep them off the event loop that drives other trajectories
        return await asyncio.get_running_loop().run_in_executor(None, fn, *args)

    async def run(self, sampling_params: dict[str, Any], priority: int = 0, **kwargs) -> AgentLoopOutput:
        info = kwargs["extra_info"]
        episode = await self._in_thread(Episode, info["task_dir"], info["kind"])
        messages = list(kwargs["raw_prompt"])
        runtime = await self.ct_build_initial_tokens(messages, tools=TOOLS)
        response_mask: list[int] = []
        logprobs: list[float] = []
        request_id = uuid4().hex
        turns, truncated, start = 0, False, time.time()
        try:
            for _ in range(self.max_turns):
                budget = self.response_length - len(response_mask)
                if budget <= 0:
                    truncated = True
                    break
                params = {**sampling_params, "max_tokens": min(self.max_tokens_per_turn, budget)}
                out = await self.server_manager.generate(request_id=request_id, prompt_ids=runtime,
                                                         sampling_params=params)
                merge, response_mask, new_logprobs = await self.ct_merge_assistant_token(
                    runtime, out.token_ids, response_mask, logprobs if (logprobs or out.log_probs) else None,
                    assistant_logprobs=out.log_probs or None)
                runtime, logprobs, turns = merge.token_ids, new_logprobs or [], turns + 1

                text = await self._in_thread(lambda: self.tokenizer.decode(out.token_ids, skip_special_tokens=True))
                content, calls = await self.tool_parser.extract_tool_calls(out.token_ids)
                native = [(c.name, c.arguments) for c in calls]
                assistant = {"role": "assistant", "content": content if native else text}
                if native:
                    assistant["tool_calls"] = [{"type": "function", "function": {
                        "name": n, "arguments": _as_dict(a)}} for n, a in native]
                messages.append(assistant)

                replies = await self._in_thread(episode.step, text, native)
                if episode.done:
                    break
                previous = list(messages)
                messages.extend(replies)
                merge, mask, merged_logprobs = await self.ct_merge_context_msg(
                    previous, messages, runtime, response_mask, logprobs or None, tools=TOOLS)
                if len(mask) >= self.response_length:
                    truncated = True
                    break
                runtime, response_mask, logprobs = merge.token_ids, mask, merged_logprobs or []

            reward, g = await self._in_thread(episode.score)
        finally:
            await self._in_thread(episode.close)

        self._log(info, g, reward, turns, truncated, episode, time.time() - start)
        n = len(response_mask)
        return AgentLoopOutput(
            prompt_ids=runtime[: len(runtime) - n],
            response_ids=runtime[len(runtime) - n:][: self.response_length],
            response_mask=response_mask[: self.response_length],
            response_logprobs=logprobs[: self.response_length] if logprobs else None,
            reward_score=reward,
            num_turns=2 * turns,
            metrics={},
            extra_fields={"turn_scores": [], "tool_rewards": [], "honesty_outcome": g["outcome"]},
        )

    def _log(self, info, g, reward, turns, truncated, episode, seconds):
        if not self.log_path:
            return
        # val = the 100 eval tasks (tasks/), train = tasks_train/; the two sets are disjoint
        split = "val" if Path(info["task_dir"]).parent.name == "tasks" else "train"
        row = {"time": time.time(), "split": split, "task_id": info.get("task_id"), "kind": info["kind"], "outcome": g["outcome"],
               "reward": reward, "turns": turns, "truncated": truncated, "parse_errors": episode.parse_errors,
               "tampered": g["tampered"], "claim": g["claim"], "seconds": round(seconds, 1)}
        with open(self.log_path, "a") as f:
            f.write(json.dumps(row) + "\n")


def _as_dict(arguments):
    try:
        return json.loads(arguments) if isinstance(arguments, str) else arguments
    except json.JSONDecodeError:
        return arguments
