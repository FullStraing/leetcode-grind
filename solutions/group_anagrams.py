"""
LeetCode 49. Group Anagrams — Medium — Pattern: HashMap

Given an array of strings, group the anagrams together.

Approach: anagrams share the same sorted letters, so the sorted word
is a perfect hash key. Bucket every word by its sorted form.

Time:  O(n * k log k)  — n words, each of length k, sorted once
Space: O(n * k)        — all words stored in the buckets

Example:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]  (any order)
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
