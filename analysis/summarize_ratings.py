#!/usr/bin/env python3
"""Summarize owner-entered rubric scores; never evaluate media."""

from __future__ import annotations

import argparse
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "ratings" / "owner-ratings.csv"
DEFAULT_OUTPUT = ROOT / "reports" / "summary-by-criterion.csv"
REQUIRED = {"module", "criterion", "criterion_score"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.exists():
        print(f"Input file not found: {args.input}", file=sys.stderr)
        return 2

    groups: dict[tuple[str, str], list[int]] = defaultdict(list)
    skipped_blank = 0
    skipped_invalid = 0
    try:
        with args.input.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fields = set(reader.fieldnames or [])
            missing = REQUIRED - fields
            if missing:
                print("Missing required columns: " + ", ".join(sorted(missing)), file=sys.stderr)
                return 2
            for row in reader:
                raw = (row.get("criterion_score") or "").strip()
                if not raw:
                    skipped_blank += 1
                    continue
                try:
                    score = int(raw)
                except ValueError:
                    skipped_invalid += 1
                    continue
                if score < 1 or score > 5:
                    skipped_invalid += 1
                    continue
                module = (row.get("module") or "").strip()
                criterion = (row.get("criterion") or "").strip()
                if not module or not criterion:
                    skipped_invalid += 1
                    continue
                groups[(module, criterion)].append(score)
    except OSError as exc:
        print(f"Could not read input: {exc}", file=sys.stderr)
        return 2

    if not groups:
        print(
            "No valid numeric ratings found. No summary was created. "
            f"Blank rows skipped: {skipped_blank}; invalid rows skipped: {skipped_invalid}."
        )
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    columns = ["module", "criterion", "n", "mean", "median", "minimum", "maximum"]
    try:
        with args.output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns)
            writer.writeheader()
            for (module, criterion), scores in sorted(groups.items()):
                writer.writerow({
                    "module": module,
                    "criterion": criterion,
                    "n": len(scores),
                    "mean": f"{statistics.mean(scores):.2f}",
                    "median": f"{statistics.median(scores):.2f}",
                    "minimum": min(scores),
                    "maximum": max(scores),
                })
    except OSError as exc:
        print(f"Could not write output: {exc}", file=sys.stderr)
        return 2

    print(
        f"Summary written to {args.output}. "
        f"Valid ratings: {sum(map(len, groups.values()))}; "
        f"blank rows skipped: {skipped_blank}; invalid rows skipped: {skipped_invalid}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
