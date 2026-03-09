#!/usr/bin/env python3
import csv
from pathlib import Path

csv_path = Path(__file__).resolve().parent.parent / "datasets" / "sample_tasks.csv"
with csv_path.open("r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print(f"Loaded {len(rows)} tasks:")
for row in rows:
    print(f"- {row['task_id']}: {row['category']} ({row['difficulty']})")
