"""Tests for grind.py — run with: python -m unittest -v"""
import unittest
from datetime import date, timedelta

import grind


def entry(days_ago: int, pattern: str = "hashmap", title: str = "Two Sum",
          difficulty: str = "easy", review: bool = False) -> dict:
    return {
        "title": title,
        "difficulty": difficulty,
        "pattern": pattern,
        "minutes": 15,
        "date": (date.today() - timedelta(days=days_ago)).isoformat(),
        "review": review,
    }


class TestStreaks(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(grind.current_streak([]), 0)
        self.assertEqual(grind.longest_streak([]), 0)

    def test_three_day_streak(self):
        entries = [entry(0), entry(1), entry(2)]
        self.assertEqual(grind.current_streak(entries), 3)
        self.assertEqual(grind.longest_streak(entries), 3)

    def test_gap_breaks_streak(self):
        entries = [entry(0), entry(2), entry(3), entry(4)]
        self.assertEqual(grind.current_streak(entries), 1)
        self.assertEqual(grind.longest_streak(entries), 3)

    def test_streak_alive_from_yesterday(self):
        entries = [entry(1), entry(2)]
        self.assertEqual(grind.current_streak(entries), 2)


class TestSuggestion(unittest.TestCase):
    def test_least_touched_pattern_wins(self):
        entries = [entry(0, "hashmap"), entry(1, "hashmap"),
                   entry(2, "two-pointers")]
        # everything else is at 0; earliest in learning order among
        # untouched patterns after hashmap/two-pointers is sliding-window
        self.assertEqual(grind.suggest_next_pattern(entries), "sliding-window")

    def test_stats_shape(self):
        s = grind.stats([entry(0, review=True), entry(1, difficulty="medium")])
        self.assertEqual(s["total"], 2)
        self.assertEqual(s["by_difficulty"]["easy"], 1)
        self.assertEqual(s["by_difficulty"]["medium"], 1)
        self.assertEqual(s["review_queue"], ["Two Sum"])


class TestExport(unittest.TestCase):
    def test_summary_counts_and_sections(self):
        entries = [entry(0, "hashmap", "Two Sum", "easy"),
                   entry(1, "hashmap", "Valid Anagram", "easy", review=True),
                   entry(2, "binary-search", "Binary Search", "easy")]
        text = grind.export_summary(entries)
        self.assertIn("Total solved: **3**", text)
        self.assertIn("Current streak: **3 day(s)**", text)
        self.assertIn("- easy: 3", text)
        self.assertIn("- hashmap: 2", text)
        self.assertIn("- binary-search: 1", text)
        self.assertIn("- stack: 0", text)
        self.assertIn("Next to practise: **two-pointers**", text)
        self.assertIn("- [ ] Valid Anagram", text)

    def test_empty_summary(self):
        text = grind.export_summary([])
        self.assertIn("Total solved: **0**", text)
        self.assertIn("Current streak: **0 day(s)**", text)
        self.assertNotIn("Review queue", text)


if __name__ == "__main__":
    unittest.main()
