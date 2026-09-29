"""Rejection-sampling fine-tuning (RFT), step 3: LoRA SFT on the kept trajectories.

Loss covers assistant turns only (tool results, nudges and the task prompt are context). The LoRA
config matches scripts/grpo_honesty.sh (rank 32, alpha 32, all linear layers) so RFT and GRPO differ
in the training signal, not in capacity. Saves the adapter only; vLLM serves it with --enable-lora.

Usage: python rl/rft_train.py --model <Qwen2.5-Coder-3B-Instruct> --data data/rft/sft.jsonl --out <dir>
       torchrun --nproc_per_node 4 rl/rft_train.py ...   # DDP: same global batch (--grad-accum) split across GPUs
       python rl/rft_train.py --model <path> --data data/rft/sft.jsonl --check   # masking check, no training
"""
import argparse
import json
import math
import os
import random
import sys
import time
from pathlib import Path

import torch
import torch.distributed as dist
from peft import LoraConfig, get_peft_model
from torch.nn.parallel import DistributedDataParallel as DDP
from transformers import AutoModelForCausalLM, AutoTokenizer, get_cosine_schedule_with_warmup

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from agent import TOOLS  # noqa: E402


def encode(tokenizer, messages, max_len):
    """Token ids plus labels that are -100 everywhere except assistant turns (including their <|im_end|>).

    Each assistant span is located by rendering the conversation up to that turn: the tokens between
    the prompt-with-generation-header and the prompt-plus-this-reply. Returns None if the template is not
    prefix-consistent at a turn boundary or the sample is too long.
    """
    def render(msgs, gen=False):
        out = tokenizer.apply_chat_template(msgs, tools=TOOLS, tokenize=True, add_generation_prompt=gen)
        # transformers 5.x returns a BatchEncoding here; 4.x returned the id list
        return list(out["input_ids"]) if hasattr(out, "keys") else list(out)
    ids = render(messages)
    if len(ids) > max_len:
        return None
    labels = [-100] * len(ids)
    for k, m in enumerate(messages):
        if m["role"] != "assistant":
            continue
        start, upto = render(messages[:k], gen=True), render(messages[: k + 1])
        if ids[: len(upto)] != upto or upto[: len(start)] != start:
            return None
        labels[len(start):len(upto)] = ids[len(start):len(upto)]
    return ids, labels


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", default="output/rft_lora")
    ap.add_argument("--epochs", type=int, default=2)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--grad-accum", type=int, default=16)
    ap.add_argument("--max-len", type=int, default=9216)  # same context budget as GRPO rollouts
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--check", action="store_true", help="only encode the data and report masking stats")
    args = ap.parse_args()
    random.seed(args.seed)
    torch.manual_seed(args.seed)

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    rows = [json.loads(line) for line in open(args.data)]
    samples, dropped = [], 0
    for r in rows:
        enc = encode(tokenizer, r["messages"], args.max_len)
        if enc is None:
            dropped += 1
        else:
            samples.append(enc)
    trained = sum(sum(l != -100 for l in labels) for _, labels in samples)
    total = sum(len(ids) for ids, _ in samples)
    print(json.dumps({"rows": len(rows), "encoded": len(samples), "dropped": dropped,
                      "tokens": total, "assistant_tokens": trained}), flush=True)
    if not samples:
        sys.exit("no sample survived encoding; refusing to save an untrained adapter")
    if args.check:
        ids, labels = samples[0]
        spans = [tokenizer.decode([t for t, l in zip(ids, labels) if l != -100])]
        print("trained text of sample 0:\n" + spans[0][:1500])
        return

    # DDP when launched by torchrun: every rank sees the same shuffle and takes every world-th sample, and
    # accumulates grad_accum/world samples, so one optimizer step still averages over grad_accum samples.
    world = int(os.environ.get("WORLD_SIZE", 1))
    rank = int(os.environ.get("RANK", 0))
    if world > 1:
        dist.init_process_group("nccl")
        torch.cuda.set_device(int(os.environ["LOCAL_RANK"]))
        assert args.grad_accum % world == 0, "--grad-accum must be divisible by the number of GPUs"
        samples = samples[: len(samples) // world * world]  # equal count per rank, or DDP hangs
    accum = args.grad_accum // world
    main_rank = rank == 0

    model = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=torch.bfloat16, attn_implementation="sdpa").cuda()
    model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
    model.enable_input_require_grads()
    model = get_peft_model(model, LoraConfig(r=32, lora_alpha=32, lora_dropout=0.0, target_modules="all-linear",
                                             task_type="CAUSAL_LM"))
    if main_rank:
        model.print_trainable_parameters()
    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(params, lr=args.lr, weight_decay=0.0)
    steps = math.ceil(len(samples) * args.epochs / args.grad_accum)
    scheduler = get_cosine_schedule_with_warmup(optimizer, max(1, steps // 20), steps)
    log = Path(args.out) / "train_log.jsonl"
    log.parent.mkdir(parents=True, exist_ok=True)
    net = DDP(model, device_ids=[torch.cuda.current_device()]) if world > 1 else model

    net.train()
    per_rank = len(samples) // world
    step, micro, running, start = 0, 0, 0.0, time.time()
    for epoch in range(args.epochs):
        random.shuffle(samples)  # same seed on every rank, so the shards below do not overlap
        for ids, labels in samples[rank::world]:
            ids_t = torch.tensor([ids], device="cuda")
            labels_t = torch.tensor([labels], device="cuda")
            micro += 1
            last = micro % accum == 0 or micro == per_rank * args.epochs
            sync = net.no_sync() if world > 1 and not last else torch.enable_grad()
            with sync:
                # mean over this sample's assistant tokens, then averaged over the accumulation window
                loss = net(input_ids=ids_t, labels=labels_t).loss / accum
                loss.backward()
            running += loss.item()
            if last:
                torch.nn.utils.clip_grad_norm_(params, 1.0)
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad(set_to_none=True)
                step += 1
                if world > 1:
                    r = torch.tensor([running], device="cuda")
                    dist.all_reduce(r)
                    running = r.item() / world
                if main_rank:
                    row = {"step": step, "epoch": epoch, "loss": round(running, 4), "lr": scheduler.get_last_lr()[0],
                           "seconds": round(time.time() - start), "gpus": world}
                    print(json.dumps(row), flush=True)
                    with open(log, "a") as f:
                        f.write(json.dumps(row) + "\n")
                running = 0.0
    if main_rank:
        model.save_pretrained(args.out)
        tokenizer.save_pretrained(args.out)
        print(f"saved adapter to {args.out}", flush=True)
    if world > 1:
        dist.barrier()
        dist.destroy_process_group()


if __name__ == "__main__":
    main()
