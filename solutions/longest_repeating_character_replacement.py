"""
LeetCode 424. Longest Repeating Character Replacement — Medium
Pattern: Sliding Window

Given a string `s` and an integer `k`, you may change at most `k`
characters to any other uppercase letter. Return the length of the
longest substring containing the same letter after at most `k`
replacements.

Approach: sliding window with a frequency count. Inside any window,
the cheapest way to make all letters equal is to keep the most
frequent letter and replace the rest — that costs
(window length - max frequency) replacements. Expand the right edge;
while the cost exceeds `k`, shrink from the left. Track the largest
window that fits the budget.

Time:  O(n)   — each character enters and leaves the window once
Space: O(1)   — at most 26 letter counts

Example:
    character_replacement("ABAB", 2)     -> 4
    character_replacement("AABABBA", 1)  -> 4
    character_replacement("AAAA", 0)     -> 4
    character_replacement("ABBB", 2)     -> 4
"""


def character_replacement(s: str, k: int) -> int:
    counts: dict[str, int] = {}
    best = 0
    left = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while (right - left + 1) - max(counts.values()) > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
