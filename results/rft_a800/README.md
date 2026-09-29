# RFT baseline on Qwen2.5-Coder-3B-Instruct (4 × A800, 2026-09-29)

Rejection-sampling fine-tuning: sample the base model, keep reward +1 trajectories, LoRA SFT on them.
Pipeline: `scripts/gpu_rft4.sh` (4 GPUs; `scripts/gpu_rft.sh` is the 1-GPU version).
Adapter: [huggingface.co/liangyue36/qwen2.5-coder-3b-honesty-rft](https://huggingface.co/liangyue36/qwen2.5-coder-3b-honesty-rft).

## Steps

1. Sample: base model, baseline prompt, T = 1.0, 8 passes over the 260 training tasks → 2,079 trajectories.
2. Keep reward +1 (solved, or honest "cannot" on an impossible task), at most 2 per task → 275 kept
   (107 solved, 168 honest refusals). See `build_summary.json`.
3. LoRA SFT (`rl/rft_train.py`): rank 32, alpha 32, all linear layers, assistant tokens only, 2 epochs,
   lr 1e-4, global batch 16, DDP on 4 GPUs → 34 optimizer steps (`train_log.jsonl`).
4. Evaluate base and RFT on the 100 eval tasks, T = 0.7, 4 passes each (`summaries/`).

## Result (totals over 4 passes)

| Outcome | Base | RFT |
|---|---|---|
| Feasible (240 attempts): solved | 42 | 39 |
| Feasible: "cannot" | 52 | 201 |
| Feasible: tampered | 31 | 0 |
| Feasible: false "done" | 31 | 0 |
| Feasible: no finish | 84 | 0 |
| Impossible (160 attempts): honest "cannot" | 38 | 159 |
| Impossible: tampered | 12 | 0 |
| Impossible: false "done" | 30 | 0 |
| Impossible: no finish | 80 | 1 |

Tampering plus false completion: 104 → 0 across 400 attempts. Refusals on feasible tasks: 52 → 201 of 240.
RFT removes dishonest outcomes and keeps the solve rate, but the kept data is 61% refusals and the model learns
to refuse feasible tasks (over-refusal). One training run; evaluation has 4 passes.

## Files

- `agent_rft_3b.tgz`: full artifacts (per-task results and traces, logs), as packed on the GPU box
- `summaries/`: `summary.json` of every sample and eval pass
- `build_summary.json`, `train_log.jsonl`, `timing_rft.log`

## Note on a discarded attempt

The first training attempt saved an untrained adapter: under transformers 5.x `apply_chat_template(tokenize=True)`
returns a `BatchEncoding`, the prefix check failed, and all 275 rows were dropped. `rl/rft_train.py` now handles
both return types and exits if no row survives encoding. That adapter and its evaluation were discarded.
