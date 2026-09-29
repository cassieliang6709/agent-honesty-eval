#!/bin/bash
# RFT on 4 GPUs (same stages and outputs as gpu_rft.sh, which runs on 1 GPU):
#   one vLLM server per GPU (ports 8000-8003); independent passes run in parallel.
#   GPU k: sample passes k and k+4 (T=1.0), then base eval pass k (T=0.7).
#   Train with DDP on all 4 GPUs (falls back to GPU 0); then RFT eval pass k on GPU k.
export PATH=/root/miniconda3/bin:$PATH   # vLLM JIT-compiles kernels at startup and needs ninja on PATH
cd /root/autodl-tmp/agent-honesty-eval; mkdir -p runs logs data/rft
PY=${PY:-/root/miniconda3/bin/python}
TRAIN_PY=${TRAIN_PY:-/root/autodl-tmp/envverl/bin/python}
VLLM=${VLLM:-/root/miniconda3/bin/vllm}
M=/root/autodl-tmp/models/Qwen2.5-Coder-3B-Instruct
ADAPTER=/root/autodl-tmp/output/honesty/rft_3b
WORKERS=${WORKERS:-24}
T=logs/timing_rft.log
t() { local n=$1; shift; local S=$(date +%s); "$@"; local rc=$?; echo "[$(date +%T)] $n $(( $(date +%s)-S ))s rc=$rc" >> $T; return $rc; }
done_run() { [ -f "$1/summary.json" ]; }
serve_all() {  # serve_all [extra vllm args...]
  for g in 0 1 2 3; do
    CUDA_VISIBLE_DEVICES=$g $VLLM serve $M --served-model-name qwen-coder-3b --enable-auto-tool-choice --tool-call-parser hermes \
      --max-model-len 16384 --gpu-memory-utilization 0.9 --port 800$g "$@" > logs/vllm_rft_g$g.log 2>&1 < /dev/null &
  done
  for g in 0 1 2 3; do for i in $(seq 1 90); do curl -s localhost:800$g/v1/models > /dev/null && break
    grep -q "Engine core initialization failed" logs/vllm_rft_g$g.log && break; sleep 10; done; done
  echo "[$(date +%T)] vllm up: $(for g in 0 1 2 3; do curl -s -o /dev/null -w '%{http_code} ' localhost:800$g/v1/models; done)" >> $T
  for g in 0 1 2 3; do curl -s localhost:800$g/v1/models > /dev/null || return 1; done   # fail fast, do not burn GPU time
}
stop_serve() { pkill -f "[b]in/vllm serve"; sleep 20; }
evaluate() {  # evaluate <port> <served model> <tasks> <out> <temperature>
  done_run "$4" || t "$(basename $4)" $PY src/run_eval.py --base-url http://localhost:$1/v1 --model "$2" \
    --prompt baseline --tasks "$3" --out "$4" --workers $WORKERS --temperature "$5" > logs/$(basename $4).log 2>&1
}
finish() {
  tar czf /root/autodl-tmp/agent_rft_3b.tgz --exclude='runs/*/work' runs/rft_* runs/baseline_3b_t07_v3_* \
    data/rft/build_summary.json $ADAPTER/train_log.jsonl logs/*rft* logs/timing_rft.log 2>/dev/null
  touch /root/autodl-tmp/$1
  sleep 900; shutdown
}
fail() { echo "[$(date +%T)] FAILED at $1" >> $T; stop_serve; finish RFT_FAILED; exit 1; }

serve_all || fail vllm_start
pids=()
for g in 0 1 2 3; do
  ( evaluate 800$g qwen-coder-3b tasks_train runs/rft_sample_$((g+1)) 1.0 && \
    evaluate 800$g qwen-coder-3b tasks_train runs/rft_sample_$((g+5)) 1.0 && \
    evaluate 800$g qwen-coder-3b tasks runs/baseline_3b_t07_v3_s$((g+1)) 0.7 ) & pids+=($!)
done
for p in "${pids[@]}"; do wait $p || fail sample_or_base_eval; done
stop_serve

[ -s data/rft/sft.jsonl ] || t build $PY rl/rft_build_sft.py --runs runs/rft_sample_* --tasks tasks_train --out data/rft/sft.jsonl \
  > logs/rft_build.log 2>&1 || fail build
# DDP on 4 GPUs (same global batch of 16); if it fails, retry on 1 GPU so the run still finishes
if [ ! -f $ADAPTER/adapter_model.safetensors ]; then
  t train_ddp4 $TRAIN_PY -m torch.distributed.run --nproc_per_node 4 rl/rft_train.py --model $M \
    --data data/rft/sft.jsonl --out $ADAPTER > logs/rft_train.log 2>&1 || {
    rm -f $ADAPTER/train_log.jsonl
    CUDA_VISIBLE_DEVICES=0 t train_1gpu $TRAIN_PY rl/rft_train.py --model $M \
      --data data/rft/sft.jsonl --out $ADAPTER > logs/rft_train_1gpu.log 2>&1 || fail train; }
fi

serve_all --enable-lora --max-lora-rank 32 --lora-modules rft-3b=$ADAPTER || fail vllm_start_lora
pids=()
for g in 0 1 2 3; do evaluate 800$g rft-3b tasks runs/rft_3b_t07_s$((g+1)) 0.7 & pids+=($!); done
for p in "${pids[@]}"; do wait $p || fail rft_eval; done
stop_serve
echo "[$(date +%T)] ALL DONE" >> $T
finish RFT_DONE
