#!/bin/bash
# 3B, both prompts, with the parser that reads all 106 turns round 2 failed on.
# serve -> eval -> pack -> DONE marker -> stop vLLM. Pre-RL numbers for the 3B model RL starts from.
cd /root/autodl-tmp/agent-honesty-eval; mkdir -p runs logs
export PATH=/root/miniconda3/bin:$PATH
T=logs/timing_3b_v3.log
t() { local n=$1; shift; local S=$(date +%s); "$@"; local rc=$?; echo "[$(date +%T)] $n $(( $(date +%s)-S ))s rc=$rc" >> $T; return $rc; }
M=/root/autodl-tmp/models/Qwen2.5-Coder-3B-Instruct
if ! curl -s localhost:8000/v1/models > /dev/null; then
  vllm serve $M --served-model-name qwen-coder-3b --enable-auto-tool-choice --tool-call-parser hermes \
    --max-model-len 16384 --gpu-memory-utilization 0.9 --port 8000 > logs/vllm_3b_v3.log 2>&1 < /dev/null &
  for i in $(seq 1 90); do curl -s localhost:8000/v1/models > /dev/null && break; sleep 10; done
fi
echo "[$(date +%T)] vllm: $(curl -s localhost:8000/v1/models | head -c 60)" >> $T
for p in baseline honesty; do
  t v3_$p python src/run_eval.py --base-url http://localhost:8000/v1 --model qwen-coder-3b --prompt $p \
    --tasks tasks --out runs/${p}_3b_t07_v3 --workers 16 --temperature 0.7 > logs/eval3b_v3_$p.log 2>&1
done
tar czf /root/autodl-tmp/agent_eval_3b_v3.tgz --exclude='runs/*/work' runs/*_3b_t07_v3 logs/*3b_v3*
echo "[$(date +%T)] PACKED" >> $T
touch /root/autodl-tmp/AGENT3B_V3_DONE
# no shutdown: the RL smoke test runs next
pkill -f "vllm serve"   # free the GPU for RL
