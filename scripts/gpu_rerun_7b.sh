#!/bin/bash
# Rerun after the tool-call parser fix, on the 7B vLLM server that is already up -> pack -> shut down.
cd /root/autodl-tmp/agent-honesty-eval
export PATH=/root/miniconda3/bin:$PATH
T=logs/timing_7b_v2.log
t() { local n=$1; shift; local S=$(date +%s); "$@"; local rc=$?; echo "[$(date +%T)] $n $(( $(date +%s)-S ))s rc=$rc" >> $T; return $rc; }
M=/root/autodl-tmp/models/Qwen2.5-Coder-7B-Instruct
if ! curl -s localhost:8000/v1/models > /dev/null; then
  vllm serve $M --served-model-name qwen-coder-7b --enable-auto-tool-choice --tool-call-parser hermes \
    --max-model-len 16384 --gpu-memory-utilization 0.9 --port 8000 > logs/vllm_7b_v2.log 2>&1 < /dev/null &
  for i in $(seq 1 90); do curl -s localhost:8000/v1/models > /dev/null && break; sleep 10; done
fi
echo "[$(date +%T)] vllm: $(curl -s localhost:8000/v1/models | head -c 60)" >> $T
for p in baseline honesty; do
  t v2_$p python src/run_eval.py --base-url http://localhost:8000/v1 --model qwen-coder-7b --prompt $p \
    --tasks tasks --out runs/${p}_7b_t07_v2 --workers 16 --temperature 0.7 > logs/eval7b_v2_$p.log 2>&1
done
tar czf /root/autodl-tmp/agent_eval_7b_v2.tgz --exclude='runs/*/work' runs logs
echo "[$(date +%T)] PACKED" >> $T
touch /root/autodl-tmp/AGENT7B_V2_DONE
sleep 1200; shutdown
