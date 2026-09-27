#!/bin/bash
# One paid hour: GRPO budget run -> pack logs -> DONE marker -> shut down.
# The first validation (step 0) doubles as the pre-RL 3B baseline on the 100 eval tasks.
cd /root/autodl-tmp/agent-honesty-eval; mkdir -p logs
OUT=/root/autodl-tmp/output/honesty/grpo_lora_3b_budget
MODE=budget bash scripts/grpo_honesty.sh > logs/grpo_budget.log 2>&1
echo "exit=$?" >> logs/grpo_budget.log
tar czf /root/autodl-tmp/rl_budget.tgz logs/grpo_budget.log $OUT/rollouts.jsonl
touch /root/autodl-tmp/RL_BUDGET_DONE
sleep 600; shutdown
