"""Run the agent on every task and grade it.

Usage: python src/run_eval.py --base-url http://localhost:8000/v1 --model qwen-coder --prompt baseline \
           --tasks tasks --out runs/baseline
Writes runs/<name>/results.jsonl (one graded run per task, with the full trajectory) and prints a summary.
"""
import argparse
import collections
import json
import shutil
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from openai import OpenAI

sys.path.insert(0, str(Path(__file__).parent))
from agent import run_agent  # noqa: E402
from grade import grade  # noqa: E402


def summarize(rows):
    by_kind = collections.defaultdict(collections.Counter)
    for r in rows:
        by_kind[r["kind"]][r["grade"]["outcome"]] += 1
        if r["kind"] != "feasible":
            by_kind["impossible (all)"][r["grade"]["outcome"]] += 1
    return {k: dict(v) for k, v in by_kind.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--prompt", default="baseline")
    ap.add_argument("--tasks", default="tasks")
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--resume", action="store_true", help="skip tasks already in results.jsonl")
    args = ap.parse_args()

    client = OpenAI(base_url=args.base_url, api_key="EMPTY")
    manifest = json.loads(Path(args.tasks, "manifest.json").read_text())
    if args.limit:
        manifest = manifest[: args.limit]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    done_rows = []
    if args.resume and (out / "results.jsonl").exists():
        done_rows = [json.loads(line) for line in open(out / "results.jsonl")]
        finished = {r["task_id"] for r in done_rows}
        manifest = [t for t in manifest if t["task_id"] not in finished]
        print(f"resuming: {len(finished)} done, {len(manifest)} to go", flush=True)
    lock = threading.Lock()
    f = open(out / "results.jsonl", "a" if args.resume else "w")

    def one(t):
        try:
            return run_one(t)
        except Exception as e:  # never let one task take down the whole run
            print(t["task_id"], "crashed", repr(e)[:200], flush=True)
            return None

    def run_one(t):
        task_dir = Path(args.tasks, t["task_id"])
        work = out / "work" / t["task_id"]
        shutil.rmtree(work, ignore_errors=True)
        shutil.copytree(task_dir, work)
        run = run_agent(client, args.model, work, prompt=args.prompt, temperature=args.temperature)
        g = grade(task_dir, work, t["kind"], (run["finish"] or {}).get("status"))
        print(t["task_id"], g["outcome"], f"turns={run['turns']}", run.get("error", ""), flush=True)
        row = {**t, "prompt": args.prompt, "model": args.model, "turns": run["turns"], "error": run.get("error"),
               "finish": run["finish"], "grade": g, "log": run["log"]}
        with lock:  # write as we go so a crash doesn't lose finished tasks
            f.write(json.dumps(row) + "\n")
            f.flush()
        return row

    with ThreadPoolExecutor(args.workers) as pool:  # vLLM batches the concurrent requests
        rows = done_rows + [r for r in pool.map(one, manifest) if r]
    f.close()
    summary = summarize(rows)
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
