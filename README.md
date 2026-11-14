# LeetCode Grind

**A daily LeetCode practice system: tested Python solutions + a CLI tracker that keeps the streak alive and tells you what to practise next.**

Built around one rule: **2 problems a day, every day** — while preparing for Summer 2027 software engineering internship interviews.

---

## What this project does

1. **Stores clean, tested solutions** — one Python module per problem in [`solutions/`](solutions/). Every module states the problem, the pattern it trains, the approach, and its time/space complexity. Every solution is covered by unit tests; a solution is not "done" until its test passes and it can be re-solved from a blank page.

2. **Tracks the grind with a CLI** — [`grind.py`](grind.py) logs solved problems to a local JSON file and answers three questions:
   - *Am I still on streak?* — current and longest streak of consecutive solving days
   - *Where are the gaps?* — breakdown by difficulty and by pattern
   - *What do I do next?* — suggests the least-practised pattern, and keeps a re-solve queue for problems flagged for spaced repetition

3. **Shows the plan and the history** — [`ROADMAP.md`](ROADMAP.md) lists the 12 interview patterns in learning order with their status, and [`PROGRESS.md`](PROGRESS.md) is a dated log of what landed each day.

## Quick start

No dependencies. Python 3.10+.

```bash
git clone https://github.com/FullStraing/leetcode-grind.git
cd leetcode-grind

# log a solved problem
python grind.py add "Two Sum" easy hashmap --minutes 12
python grind.py add "Group Anagrams" medium hashmap --minutes 25 --review

# see where you stand
python grind.py stats
python grind.py next      # which pattern to practise next
python grind.py review    # problems flagged for re-solving

# run all tests (tracker + every solution)
python -m unittest -v
```

Example output:

```
$ python grind.py stats
Total solved:    15
Current streak:  3 day(s)
Longest streak:  5 day(s)
By difficulty:   easy 10 · medium 5 · hard 0
By pattern:      binary-search 4, two-pointers 4, hashmap 3, ...
Next to practise: sliding-window
```

## Solutions so far

| # | Problem | Difficulty | Pattern | Approach in one line |
|---|---------|-----------|---------|----------------------|
| 1 | [Two Sum](solutions/two_sum.py) | Easy | HashMap | One pass, look up `target - num` |
| 3 | [Longest Substring Without Repeating Characters](solutions/longest_substring.py) | Medium | Sliding Window | Window expands right, jumps left past repeats |
| 49 | [Group Anagrams](solutions/group_anagrams.py) | Medium | HashMap | Bucket words by their sorted letters |
| 167 | [Two Sum II](solutions/two_sum_ii.py) | Medium | Two Pointers | Sorted array: pointers from both ends |
| 217 | [Contains Duplicate](solutions/contains_duplicate.py) | Easy | HashMap | One pass, remember what was seen |
| 242 | [Valid Anagram](solutions/valid_anagram.py) | Easy | HashMap | Count letters of one, spend on the other |
| 704 | [Binary Search](solutions/binary_search.py) | Easy | Binary Search | Halve the interval every step |

New solutions land daily — see [`PROGRESS.md`](PROGRESS.md).

## Project structure

```
leetcode-grind/
├── README.md          ← you are here
├── grind.py           ← CLI tracker: streaks, stats, next pattern, review queue
├── test_grind.py      ← tests for the tracker
├── solutions/         ← one tested module per solved problem
│   ├── two_sum.py
│   ├── valid_anagram.py
│   ├── group_anagrams.py
│   ├── contains_duplicate.py
│   ├── longest_substring.py
│   ├── binary_search.py
│   └── two_sum_ii.py
├── test_solutions.py  ← tests for every solution
├── ROADMAP.md         ← the 12 patterns, in order, with status
└── PROGRESS.md        ← dated daily log — the streak, in writing
```

## Why it exists

Interview prep usually dies from missed days, not from hard problems.
This repo makes the streak visible, the gaps obvious, and the next
step automatic — so the only daily decision left is *sit down and solve*.

## License

MIT — see [`LICENSE`](LICENSE).
