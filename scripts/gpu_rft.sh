#!/bin/bash
# RFT on one GPU, unattended:
#   1. sample: base 3B, baseline prompt, T=1.0 (the GRPO rollout temperature), 8 passes over tasks_train/
#   2. base eval: base 3B on the 100 eval tasks, T=0.7, 4 passes (also the pre-RL baseline for GRPO/GSPO)
#   3. build SFT data from reward +1 trajectories (rl/rft_build_sft.py)
#   4. LoRA SFT (rl/rft_train.py)
#   5. RFT eval: base + adapter on the 100 eval tasks, T=0.7, 4 passes
# then pack -> DONE (or FAILED) marker -> shut down 20 min later (time for the Mac to pull results).
# Stages whose output already exists are skipped, so a rerun resumes.
cd /root/autodl-tmp/agent-honesty-eval; mkdir -p runs logs data/rft
PY=${PY:-/root/miniconda3/bin/python}                         # eval + builder: openai, pytest
TRAIN_PY=${TRAIN_PY:-/root/autodl-tmp/envverl/bin/python}     # torch, transformers, peft
VLLM=${VLLM:-/root/autodl-tmp/envverl/bin/vllm}
M=/root/autodl-tmp/models/Qwen2.5-Coder-3B-Instruct
ADAPTER=/root/autodl-tmp/output/honesty/rft_3b
SAMPLES=${SAMPLES:-8}; EVALS=${EVALS:-4}; WORKERS=${WORKERS:-32}
T=logs/timing_rft.log
t() { local n=$1; shift; local S=$(date +%s); "$@"; local rc=$?; echo "[$(date +%T)] $n $(( $(date +%s)-S ))s rc=$rc" >> $T; return $rc; }
done_run() { [ -f "$1/summary.json" ]; }

serve() {  # serve [extra vllm args...]
  $VLLM serve $M --served-model-name qwen-coder-3b --enable-auto-tool-choice --tool-call-parser hermes \
    --max-model-len 16384 --gpu-memory-utilization 0.9 --port 8000 "$@" > logs/vllm_rft.log 2>&1 < /dev/null &
  for i in $(seq 1 90); do curl -s localhost:8000/v1/models > /dev/null && break; sleep 10; done
  echo "[$(date +%T)] vllm: $(curl -s localhost:8000/v1/models | head -c 120)" >> $T
}
stop_serve() { pkill -f "vllm serve"; sleep 20; }
evaluate() {  # evaluate <served model> <tasks> <out> <temperature>
  done_run "$3" || t "$(basename $3)" $PY src/run_eval.py --base-url http://localhost:8000/v1 --model "$1" \
    --prompt baseline --tasks "$2" --out "$3" --workers $WORKERS --temperature "$4" > logs/$(basename $3).log 2>&1
}

finish() {
  tar czf /root/autodl-tmp/agent_rft_3b.tgz --exclude='runs/*/work' runs/rft_* runs/baseline_3b_t07_v3_* \
    data/rft/build_summary.json $ADAPTER/train_log.jsonl logs/*rft* logs/timing_rft.log 2>/dev/null
  touch /root/autodl-tmp/$1
  sleep 1200; shutdown
}
fail() { echo "[$(date +%T)] FAILED at $1" >> $T; stop_serve; finish RFT_FAILED; exit 1; }

serve
for k in $(seq 1 $SAMPLES); do evaluate qwen-coder-3b tasks_train runs/rft_sample_$k 1.0 || fail sample_$k; done
for k in $(seq 1 $EVALS); do evaluate qwen-coder-3b tasks runs/baseline_3b_t07_v3_s$k 0.7 || fail base_eval_$k; done
stop_serve

t build $PY rl/rft_build_sft.py --runs runs/rft_sample_* --tasks tasks_train --out data/rft/sft.jsonl \
  > logs/rft_build.log 2>&1 || fail build
[ -f $ADAPTER/adapter_model.safetensors ] || t train $TRAIN_PY rl/rft_train.py --model $M --data data/rft/sft.jsonl \
  --out $ADAPTER > logs/rft_train.log 2>&1 || fail train

serve --enable-lora --max-lora-rank 32 --lora-modules rft-3b=$ADAPTER
for k in $(seq 1 $EVALS); do evaluate rft-3b tasks runs/rft_3b_t07_s$k 0.7 || fail rft_eval_$k; done
stop_serve
echo "[$(date +%T)] ALL DONE" >> $T
finish RFT_DONE
