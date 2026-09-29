"""Rejection-sampling fine-tuning (RFT), step 2: turn reward +1 rollouts into SFT conversations.

Reads sampled eval runs on tasks_train/ (src/run_eval.py outputs), keeps trajectories whose grader
outcome earns +1 (solved on feasible, honest_cannot on impossible), caps how many are kept per task,
and replays each one through honesty_env.Episode to rebuild the exact messages the model saw.
A trajectory is dropped if the replay grades it differently from the recorded run.

Usage: python rl/rft_build_sft.py --runs runs/rft_sample_* --tasks tasks_train --out data/rft/sft.jsonl
"""
import argparse
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from agent import PROMPTS  # noqa: E402
from honesty_env import REWARD, Episode  # noqa: E402

FIRST_USER = "The repository is ready. Start by reading TASK.md."


def arguments_dict(arguments):
    """Qwen's chat template serialises tool-call arguments with tojson, so pass a dict, not a JSON string."""
    if isinstance(arguments, str):
        try:
            return json.loads(arguments or "{}")
        except json.JSONDecodeError:
            return arguments
    return arguments


def replay(row, task_dir):
    """Rebuild the conversation for one recorded run. Returns (messages, outcome)."""
    messages = [{"role": "system", "content": PROMPTS[row["prompt"]]}, {"role": "user", "content": FIRST_USER}]
    ep = Episode(task_dir, row["kind"])
    try:
        for step in row["log"]:
            calls = step.get("tool_calls") or []
            native = [(c["function"]["name"], c["function"]["arguments"]) for c in calls]
            assistant = {"role": "assistant", "content": step.get("content") or ""}
            if native:
                assistant["tool_calls"] = [{"type": "function", "function": {"name": n, "arguments": arguments_dict(a)}}
                                           for n, a in native]
            messages.append(assistant)
            replies = ep.step(step.get("content") or "", native)
            if ep.done:
                break
            messages.extend(replies)
        _, g = ep.score()
    finally:
        ep.close()
    return messages, g["outcome"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True, help="run dirs, each with results.jsonl")
    ap.add_argument("--tasks", default="tasks_train")
    ap.add_argument("--out", default="data/rft/sft.jsonl")
    ap.add_argument("--per-task", type=int, default=2, help="max kept trajectories per task")
    args = ap.parse_args()

    rows = [json.loads(line) for run in args.runs for line in open(Path(run) / "results.jsonl")]
    sampled = collections.Counter(r["grade"]["outcome"] for r in rows)
    kept, per_task, stats = [], collections.Counter(), collections.Counter()
    for r in rows:
        outcome = r["grade"]["outcome"]
        if r.get("error") or REWARD[outcome] != 1.0:
            continue
        if per_task[r["task_id"]] >= args.per_task:
            stats["over_cap"] += 1
            continue
        messages, replayed = replay(r, ROOT / args.tasks / r["task_id"])
        if replayed != outcome:
            stats["replay_mismatch"] += 1
            continue
        per_task[r["task_id"]] += 1
        stats[f"kept_{outcome}"] += 1
        kept.append({"task_id": r["task_id"], "kind": r["kind"], "outcome": outcome, "messages": messages})

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        for k in kept:
            f.write(json.dumps(k, ensure_ascii=False) + "\n")
    summary = {"sampled": len(rows), "sampled_outcomes": dict(sampled), **stats,
               "kept": len(kept), "tasks_with_data": len(per_task)}
    (out.parent / "build_summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
