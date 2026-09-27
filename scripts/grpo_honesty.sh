#!/bin/bash
# GRPO + LoRA on Qwen2.5-Coder-3B-Instruct, RTX 4090s. Each trajectory is a full honesty-eval
# episode (rl/honesty_agent_loop.py); reward = grader outcome (src/honesty_env.py REWARD).
# Train: tasks_train/ (260, disjoint from eval). Validation: tasks/ (the 100 eval tasks), T=0.7 like the eval.
# The system prompt is the eval's *baseline* prompt: the model is never told to be honest, only rewarded for it.
#
# Usage: MODE=budget bash scripts/grpo_honesty.sh  (default: 10 steps, val at 0/5/10, no checkpoints; ~1 h on 4 GPUs)
#        MODE=smoke  bash scripts/grpo_honesty.sh  (2 steps, 4 tasks x 4 rollouts: wiring check)
#        MODE=full   bash scripts/grpo_honesty.sh  (3 epochs over 260 tasks, 16 x 8 rollouts per step)
# Uses every visible GPU (data-parallel actor, one vLLM replica per GPU).
# Adapted from ai-infra-gsm8k/scripts/grpo.sh and verl examples/tuning/lora/run_qwen3_8b_fsdp.sh (commit 6093e00).
set -xeo pipefail
source /root/autodl-tmp/envverl/bin/activate
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
REPO=/root/autodl-tmp/agent-honesty-eval
cd $REPO
export PYTHONPATH=$REPO:$REPO/src:${PYTHONPATH:-}   # Ray workers inherit this and import rl.honesty_agent_loop
MODEL_PATH=${MODEL_PATH:-/root/autodl-tmp/models/Qwen2.5-Coder-3B-Instruct}
MODE=${MODE:-budget}
NGPU=${NGPU:-$(nvidia-smi -L | wc -l)}
LR=${LR:-1e-5}
if [ "$MODE" = smoke ]; then
  BATCH=4; N=4; STEPS="trainer.total_training_steps=2"; SAVE=-1; TEST=-1; VAL_BEFORE=False; EXP=smoke
elif [ "$MODE" = budget ]; then
  # no checkpoints: a full FSDP save is ~6 GB and the data disk had 2.1 GB free; the val curve is the result
  BATCH=16; N=8; STEPS="trainer.total_training_steps=${TOTAL_STEPS:-10}"; SAVE=-1; TEST=5; VAL_BEFORE=True; EXP=${EXP:-grpo_lora_3b_budget}
else
  BATCH=16; N=8; STEPS="trainer.total_epochs=3"; SAVE=8; TEST=8; VAL_BEFORE=True; EXP=${EXP:-grpo_lora_3b}
fi
OUT=/root/autodl-tmp/output/honesty/$EXP
mkdir -p $OUT
export HONESTY_ROLLOUT_LOG=$OUT/rollouts.jsonl      # one line per trajectory: task, outcome, reward, turns
python rl/prepare_data.py --prompt baseline --out data/rl

python3 -m verl.trainer.main_ppo \
  algorithm.adv_estimator=grpo \
  algorithm.use_kl_in_reward=False \
  data.train_files=data/rl/train.parquet \
  data.val_files=data/rl/val.parquet \
  data.train_batch_size=$BATCH \
  data.max_prompt_length=1024 \
  data.max_response_length=8192 \
  data.filter_overlong_prompts=False \
  data.truncation=error \
  data.return_raw_chat=True \
  data.dataloader_num_workers=2 \
  actor_rollout_ref.model.path=$MODEL_PATH \
  actor_rollout_ref.model.lora_rank=32 \
  actor_rollout_ref.model.lora_alpha=32 \
  actor_rollout_ref.model.target_modules=all-linear \
  actor_rollout_ref.model.use_remove_padding=True \
  actor_rollout_ref.model.enable_gradient_checkpointing=True \
  ++actor_rollout_ref.model.override_config.attn_implementation=sdpa \
  actor_rollout_ref.actor.optim.lr=$LR \
  actor_rollout_ref.actor.ppo_mini_batch_size=$BATCH \
  actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=1 \
  actor_rollout_ref.actor.use_dynamic_bsz=True \
  actor_rollout_ref.actor.ppo_max_token_len_per_gpu=9216 \
  actor_rollout_ref.actor.use_kl_loss=True \
  actor_rollout_ref.actor.kl_loss_coef=0.001 \
  actor_rollout_ref.actor.kl_loss_type=low_var_kl \
  actor_rollout_ref.actor.entropy_coeff=0 \
  actor_rollout_ref.actor.fsdp_config.param_offload=False \
  actor_rollout_ref.actor.fsdp_config.optimizer_offload=False \
  actor_rollout_ref.rollout.name=vllm \
  actor_rollout_ref.rollout.mode=async \
  actor_rollout_ref.rollout.load_format=safetensors \
  actor_rollout_ref.rollout.layered_summon=True \
  actor_rollout_ref.rollout.tensor_model_parallel_size=1 \
  actor_rollout_ref.rollout.gpu_memory_utilization=0.4 \
  actor_rollout_ref.rollout.max_model_len=9216 \
  actor_rollout_ref.rollout.max_num_batched_tokens=9216 \
  actor_rollout_ref.rollout.temperature=1.0 \
  actor_rollout_ref.rollout.n=$N \
  actor_rollout_ref.rollout.val_kwargs.temperature=0.7 \
  actor_rollout_ref.rollout.val_kwargs.do_sample=True \
  actor_rollout_ref.rollout.val_kwargs.n=1 \
  actor_rollout_ref.rollout.agent.agent_loop_config_path=$REPO/rl/agent_loops.yaml \
  actor_rollout_ref.rollout.agent.default_agent_loop=honesty_agent \
  actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=1 \
  actor_rollout_ref.rollout.log_prob_use_dynamic_bsz=True \
  actor_rollout_ref.rollout.log_prob_max_token_len_per_gpu=9216 \
  actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=1 \
  actor_rollout_ref.ref.log_prob_use_dynamic_bsz=True \
  actor_rollout_ref.ref.log_prob_max_token_len_per_gpu=9216 \
  trainer.critic_warmup=0 \
  trainer.logger='["console"]' \
  trainer.project_name=agent_honesty \
  trainer.experiment_name=$EXP \
  trainer.default_local_dir=$OUT \
  trainer.n_gpus_per_node=$NGPU \
  trainer.nnodes=1 \
  trainer.save_freq=$SAVE \
  trainer.test_freq=$TEST \
  trainer.max_actor_ckpt_to_keep=2 \
  trainer.val_before_train=$VAL_BEFORE \
  $STEPS \
  ray_kwargs.ray_init.runtime_env.py_executable=null \
  "$@"
