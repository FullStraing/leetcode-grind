"""
LeetCode 3. Longest Substring Without Repeating Characters — Medium
Pattern: Sliding Window

Given a string `s`, find the length of the longest substring without
repeating characters.

Approach: sliding window with two pointers. The right pointer expands
the window one character at a time; the left pointer jumps past the
previous occurrence of any repeated character, so the window always
holds distinct characters. Track the widest window seen.

Time:  O(n)   — each character visited at most twice
Space: O(k)   — k = size of the alphabet actually used

Example:
    length_of_longest_substring("abcabcbb") -> 3   ("abc")
    length_of_longest_substring("bbbbb")    -> 1   ("b")
    length_of_longest_substring("pwwkew")   -> 3   ("wke")
"""


def length_of_longest_substring(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
