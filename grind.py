#!/usr/bin/env python3
"""
grind — a tiny CLI to keep a daily LeetCode grind alive.

Logs solved problems to a local JSON file, computes your current
streak (consecutive days with >= 1 solve) and suggests what pattern
to practise next, based on which patterns you have touched least.

No dependencies. Python 3.10+.

Examples:
    python grind.py add "Two Sum" easy hashmap
    python grind.py add "Group Anagrams" medium hashmap --minutes 25
    python grind.py stats
    python grind.py next
    python grind.py review
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).with_name("grind_data.json")

# Core patterns for SWE interviews, roughly in learning order.
PATTERNS = [
    "hashmap",
    "two-pointers",
    "sliding-window",
    "binary-search",
    "stack",
    "linked-list",
    "trees",
    "graphs",
    "heap",
    "backtracking",
    "dynamic-programming",
    "greedy",
]

DIFFICULTIES = ("easy", "medium", "hard")


def load_entries(path: Path = DATA_FILE) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


def save_entries(entries: list[dict], path: Path = DATA_FILE) -> None:
    path.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def add_entry(entries: list[dict], title: str, difficulty: str,
              pattern: str, minutes: int | None = None,
              on: date | None = None, review: bool = False) -> dict:
    entry = {
        "title": title.strip(),
        "difficulty": difficulty.lower(),
        "pattern": pattern.lower(),
        "minutes": minutes,
        "date": (on or date.today()).isoformat(),
        "review": bool(review),
    }
    entries.append(entry)
    return entry


def current_streak(entries: list[dict], today: date | None = None) -> int:
    """Consecutive days ending today (or yesterday) with at least one solve."""
    days = {e["date"] for e in entries}
    if not days:
        return 0
    cursor = today or date.today()
    # A streak is still alive if yesterday was the last active day.
    if cursor.isoformat() not in days:
        cursor -= timedelta(days=1)
    streak = 0
    while cursor.isoformat() in days:
        streak += 1
        cursor -= timedelta(days=1)
    return streak


def longest_streak(entries: list[dict]) -> int:
    days = sorted({date.fromisoformat(e["date"]) for e in entries})
    if not days:
        return 0
    best = run = 1
    for prev, cur in zip(days, days[1:]):
        run = run + 1 if (cur - prev).days == 1 else 1
        best = max(best, run)
    return best


def suggest_next_pattern(entries: list[dict]) -> str:
    """Least-practised pattern; ties break by learning order."""
    counts = Counter(e["pattern"] for e in entries)
    return min(PATTERNS, key=lambda p: (counts.get(p, 0), PATTERNS.index(p)))


def stats(entries: list[dict]) -> dict:
    by_diff = Counter(e["difficulty"] for e in entries)
    by_pattern = Counter(e["pattern"] for e in entries)
    return {
        "total": len(entries),
        "current_streak": current_streak(entries),
        "longest_streak": longest_streak(entries),
        "by_difficulty": {d: by_diff.get(d, 0) for d in DIFFICULTIES},
        "by_pattern": dict(by_pattern.most_common()),
        "review_queue": [e["title"] for e in entries if e.get("review")],
        "next_pattern": suggest_next_pattern(entries),
    }


def cmd_add(args: argparse.Namespace) -> int:
    if args.difficulty.lower() not in DIFFICULTIES:
        print(f"difficulty must be one of: {', '.join(DIFFICULTIES)}", file=sys.stderr)
        return 2
    if args.pattern.lower() not in PATTERNS:
        print(f"pattern must be one of: {', '.join(PATTERNS)}", file=sys.stderr)
        return 2
    entries = load_entries()
    entry = add_entry(entries, args.title, args.difficulty, args.pattern,
                      minutes=args.minutes, review=args.review)
    save_entries(entries)
    s = stats(entries)
    print(f"Logged: {entry['title']} ({entry['difficulty']}, {entry['pattern']})")
    print(f"Streak: {s['current_streak']} day(s) · Total solved: {s['total']}")
    return 0


def cmd_stats(_: argparse.Namespace) -> int:
    s = stats(load_entries())
    print(f"Total solved:    {s['total']}")
    print(f"Current streak:  {s['current_streak']} day(s)")
    print(f"Longest streak:  {s['longest_streak']} day(s)")
    diff = s["by_difficulty"]
    print(f"By difficulty:   easy {diff['easy']} · medium {diff['medium']} · hard {diff['hard']}")
    if s["by_pattern"]:
        print("By pattern:      " + ", ".join(f"{k} {v}" for k, v in s["by_pattern"].items()))
    print(f"Next to practise: {s['next_pattern']}")
    return 0


def cmd_next(_: argparse.Namespace) -> int:
    entries = load_entries()
    pattern = suggest_next_pattern(entries)
    print(f"Practise next: {pattern}")
    print("Why: it's your least-touched pattern so far.")
    return 0


def cmd_review(_: argparse.Namespace) -> int:
    queue = stats(load_entries())["review_queue"]
    if not queue:
        print("Review queue is empty. Flag a problem with --review when you add it.")
        return 0
    print("Re-solve these without looking at your old solution:")
    for i, title in enumerate(queue, 1):
        print(f"  {i}. {title}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="grind", description="Daily LeetCode grind tracker")
    sub = p.add_subparsers(dest="command", required=True)

    a = sub.add_parser("add", help="log a solved problem")
    a.add_argument("title")
    a.add_argument("difficulty", help="easy | medium | hard")
    a.add_argument("pattern", help="one of: " + ", ".join(PATTERNS))
    a.add_argument("--minutes", type=int, default=None)
    a.add_argument("--review", action="store_true", help="flag for spaced re-solve")
    a.set_defaults(func=cmd_add)

    s = sub.add_parser("stats", help="totals, streaks and breakdown")
    s.set_defaults(func=cmd_stats)

    n = sub.add_parser("next", help="suggest the next pattern to practise")
    n.set_defaults(func=cmd_next)

    r = sub.add_parser("review", help="show the re-solve queue")
    r.set_defaults(func=cmd_review)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
