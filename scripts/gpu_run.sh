#!/bin/bash
# One RTX 4090: download Qwen2.5-Coder-3B-Instruct, serve it with vLLM (tool calling on),
# run the baseline and honesty prompts over all 100 tasks, pack results, shut down.
cd /root/autodl-tmp/agent-honesty-eval; mkdir -p runs logs
export PATH=/root/miniconda3/bin:$PATH
T=logs/timing.log
t() { local n=$1; shift; local S=$(date +%s); "$@"; local rc=$?; echo "[$(date +%T)] $n $(( $(date +%s)-S ))s rc=$rc" >> $T; return $rc; }
M=/root/autodl-tmp/models/Qwen2.5-Coder-3B-Instruct

[ -f $M/config.json ] || t download modelscope download --model Qwen/Qwen2.5-Coder-3B-Instruct --local_dir $M > logs/download.log 2>&1
vllm serve $M --served-model-name qwen-coder-3b --enable-auto-tool-choice --tool-call-parser hermes \
  --max-model-len 16384 --gpu-memory-utilization 0.85 --port 8000 > logs/vllm.log 2>&1 &
for i in $(seq 1 90); do curl -s localhost:8000/v1/models > /dev/null && break; sleep 10; done
echo "[$(date +%T)] vllm up" >> $T

for p in baseline honesty; do
  t eval_$p python src/run_eval.py --base-url http://localhost:8000/v1 --model qwen-coder-3b \
    --prompt $p --tasks tasks --out runs/$p > logs/eval_$p.log 2>&1
done
tar czf /root/autodl-tmp/agent_eval_results.tgz --exclude='runs/*/work' runs logs
echo "[$(date +%T)] PACKED" >> $T
touch /root/autodl-tmp/AGENT_DONE
sleep 900; shutdown
