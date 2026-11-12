"""
LeetCode 1. Two Sum — Easy — Pattern: HashMap

Given an array of integers `nums` and an integer `target`, return the
indices of the two numbers that add up to `target`.

Approach: one pass. For each number, the partner we need is
`target - num`. If that partner was already seen, we are done;
otherwise store the current number with its index.

Time:  O(n)   — single pass, O(1) average hash lookups
Space: O(n)   — the seen-map holds at most n entries

Example:
    two_sum([2, 7, 11, 15], 9) -> [0, 1]
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        partner = target - num
        if partner in seen:
            return [seen[partner], i]
        seen[num] = i
    return []
