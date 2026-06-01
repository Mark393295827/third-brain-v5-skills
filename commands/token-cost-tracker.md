---
name: token-cost-tracker
description: Estimate and track token usage and cost across the knowledge pipeline. Run before expensive tasks to budget, after tasks to log actuals.
usage: "token-cost-tracker [estimate|log|report] [options]"
---

# Token Cost Tracker

Estimate, log, and report token usage across the knowledge compounding pipeline.

## Commands

### `token-cost-tracker estimate`

Estimate cost before running a task:

```
token-cost-tracker estimate --task ingest --sources 3 --avg-tokens 5000
  → Estimated: ~15K input + ~3K output = $0.06 (Sonnet)

token-cost-tracker estimate --task compile --depth deep
  → Estimated: ~200K input + ~50K output = $3.75 (Opus)
```

### `token-cost-tracker log`

Log actual usage after a task (append to `.token-log.csv`):

```csv
date,task,model,input_tokens,output_tokens,cost,notes
2026-05-06,ingest-harness-blog,sonnet-4.6,45231,8732,0.16,3 sources ingested
2026-05-06,compile-ai-agent,opus-4.6,198432,43211,5.23,7-step cognitive compile
```

### `token-cost-tracker report`

Generate weekly/monthly summary:

```
token-cost-tracker report --period weekly
  → Weekly Summary (May 4-10)
     Total tokens: 1,234,567
     Total cost:   $23.45
     Breakdown:
       Opus:    $15.20 (65%)
       Sonnet:  $7.80 (33%)
       Haiku:   $0.45 (2%)
     By task:
       ingest:      $8.20 (8 tasks)
       compile:     $10.50 (2 compiles)
       session-lrn: $2.40 (12 sessions)
       lint:        $0.35 (4 checks)
```

## Per-Task Cost Benchmarks

| Task | Model | Typical Tokens | Typical Cost |
|------|-------|:--------------:|:------------:|
| wiki-ingest (1 source) | Sonnet | 15K-50K | $0.05-0.15 |
| wiki-ingest (bulk, 5) | Sonnet | 100K-300K | $0.30-0.90 |
| cognitive-compile | Opus | 200K-500K | $3.00-7.50 |
| session-learn | Sonnet | 50K-150K | $0.15-0.45 |
| deep-research (evidence brief) | Opus | 80K-250K | $1.20-3.75 |
| deep-research (standard/heavy) | Opus | 300K-1.5M | $4.50-22.50 |
| daily-okr (full) | Sonnet+Haiku | 30K-80K | $0.10-0.25 |
| wiki-lint | Haiku | 10K-30K | $0.01-0.03 |
| context-manager | Haiku | 5K-15K | ~$0.01 |

## Python Logger Script

Save as `scripts/token-logger.py`:

```python
"""Simple token cost tracker for LLM pipeline."""
import csv, os, json
from datetime import datetime, timedelta

LOG_FILE = ".token-log.csv"
MODEL_PRICES = {
    "opus-4.6":    {"input": 15.00, "output": 75.00},
    "sonnet-4.6":  {"input": 3.00,  "output": 15.00},
    "haiku-3.5":   {"input": 0.80,  "output": 4.00},
}

def log_usage(task, model, input_tokens, output_tokens, notes=""):
    cost = (input_tokens / 1e6 * MODEL_PRICES[model]["input"] +
            output_tokens / 1e6 * MODEL_PRICES[model]["output"])
    row = [datetime.now().isoformat()[:10], task, model,
           input_tokens, output_tokens, round(cost, 4), notes]
    with open(LOG_FILE, "a", newline="") as f:
        csv.writer(f).writerow(row)
    return cost

def report(period="weekly"):
    days = 7 if period == "weekly" else 30
    cutoff = datetime.now() - timedelta(days=days)
    total_cost = 0
    task_breakdown = {}
    with open(LOG_FILE) as f:
        for row in csv.DictReader(f):
            date = datetime.strptime(row["date"], "%Y-%m-%d")
            if date < cutoff: continue
            total_cost += float(row["cost"])
            task_name = row["task"]
            task_breakdown[task_name] = task_breakdown.get(task_name, 0) + float(row["cost"])
    return {"total": round(total_cost, 2), "tasks": task_breakdown}

if __name__ == "__main__":
    import sys
    if sys.argv[1] == "report":
        print(json.dumps(report(sys.argv[2] if len(sys.argv) > 2 else "weekly"), indent=2))
```
