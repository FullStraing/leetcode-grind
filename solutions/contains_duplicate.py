"""
LeetCode 217. Contains Duplicate — Easy — Pattern: HashMap

Given an integer array `nums`, return True if any value appears at
least twice in the array, and False if every element is distinct.

Approach: scan once, remembering every value seen so far in a set.
The first repeat found ends the scan early.

Time:  O(n)   — one pass
Space: O(n)   — the set of seen values

Example:
    contains_duplicate([1, 2, 3, 1]) -> True
    contains_duplicate([1, 2, 3, 4]) -> False
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
