#!/bin/bash
# Unattended: wait for the 7B download -> swap vLLM from 3B to 7B -> 5-task smoke check ->
# baseline and honesty prompts over all 100 tasks (T=0.7, same as the 3B run) -> pack -> shut down.
cd /root/autodl-tmp/agent-honesty-eval; mkdir -p runs logs
export PATH=/root/miniconda3/bin:$PATH
T=logs/timing_7b.log
t() { local n=$1; shift; local S=$(date +%s); "$@"; local rc=$?; echo "[$(date +%T)] $n $(( $(date +%s)-S ))s rc=$rc" >> $T; return $rc; }
M=/root/autodl-tmp/models/Qwen2.5-Coder-7B-Instruct
pack() { tar czf /root/autodl-tmp/agent_eval_7b.tgz --exclude='runs/*/work' runs logs; echo "[$(date +%T)] PACKED" >> $T; }

echo "[$(date +%T)] waiting for download" >> $T
while pgrep -f "modelscope download" > /dev/null; do sleep 30; done
ls $M/*.safetensors >> $T 2>&1

pkill -f "vllm serve"; sleep 15
vllm serve $M --served-model-name qwen-coder-7b --enable-auto-tool-choice --tool-call-parser hermes \
  --max-model-len 16384 --gpu-memory-utilization 0.9 --port 8000 > logs/vllm_7b.log 2>&1 < /dev/null &
for i in $(seq 1 90); do curl -s localhost:8000/v1/models > /dev/null && break; sleep 10; done
echo "[$(date +%T)] vllm 7b up: $(curl -s localhost:8000/v1/models | head -c 80)" >> $T

t smoke python src/run_eval.py --base-url http://localhost:8000/v1 --model qwen-coder-7b --prompt baseline \
  --tasks tasks_smoke --out runs/smoke_7b --workers 5 --temperature 0.7 > logs/smoke_7b.log 2>&1
for p in baseline honesty; do
  t eval7b_$p python src/run_eval.py --base-url http://localhost:8000/v1 --model qwen-coder-7b --prompt $p \
    --tasks tasks --out runs/${p}_7b_t07 --workers 16 --temperature 0.7 > logs/eval7b_$p.log 2>&1
  pack
done
touch /root/autodl-tmp/AGENT7B_DONE
echo "[$(date +%T)] ALL DONE, shutting down in 20 min" >> $T
sleep 1200; shutdown
