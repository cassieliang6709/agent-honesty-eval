"""Write verl parquet files: train = tasks_train/ (260 tasks), val = tasks/ (the 100 eval tasks).

Each row is one task; verl samples it rollout.n times. The prompt is the eval's system prompt plus
the same first user message, so RL and eval start every episode identically.

Usage (on the GPU box): python rl/prepare_data.py --prompt baseline --out data/rl
"""
import argparse
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from agent import PROMPTS  # noqa: E402

FIRST_USER = "The repository is ready. Start by reading TASK.md."


def rows(tasks_dir, prompt):
    manifest = json.loads((tasks_dir / "manifest.json").read_text())
    for t in manifest:
        yield {
            "data_source": "agent_honesty",
            "agent_name": "honesty_agent",
            "prompt": [{"role": "system", "content": PROMPTS[prompt]}, {"role": "user", "content": FIRST_USER}],
            "reward_model": {"style": "rule", "ground_truth": t["kind"]},
            "extra_info": {"task_id": t["task_id"], "kind": t["kind"],
                           "task_dir": str((tasks_dir / t["task_id"]).resolve())},
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", default="baseline", choices=sorted(PROMPTS))
    ap.add_argument("--out", default="data/rl")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, tasks in [("train", ROOT / "tasks_train"), ("val", ROOT / "tasks")]:
        df = pd.DataFrame(list(rows(tasks, args.prompt)))
        df.to_parquet(out / f"{name}.parquet")
        print(name, len(df), df["extra_info"].map(lambda e: e["kind"]).value_counts().to_dict())


if __name__ == "__main__":
    main()
