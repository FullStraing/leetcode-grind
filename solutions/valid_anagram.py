"""
LeetCode 242. Valid Anagram — Easy — Pattern: HashMap

Given two strings `s` and `t`, return True if `t` is an anagram of `s`.

Approach: anagrams have identical character counts. Count the letters
of `s`, then spend that budget while scanning `t`; any overspend (or a
length mismatch up front) means it is not an anagram.

Time:  O(n)   — two linear scans
Space: O(k)   — k = size of the alphabet actually used

Example:
    is_anagram("anagram", "nagaram") -> True
    is_anagram("rat", "car")         -> False
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True
