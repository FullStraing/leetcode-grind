"""
LeetCode 167. Two Sum II — Input Array Is Sorted — Medium
Pattern: Two Pointers

Given a 1-indexed sorted array, find two numbers that add to `target`
and return their indices (1-indexed).

Approach: because the array is sorted, two pointers from both ends
work. Sum too small -> move the left pointer right (bigger numbers);
sum too large -> move the right pointer left.

Time:  O(n) — each pointer moves at most n steps in total
Space: O(1) — no hash map needed, sorting is the data structure

Example:
    two_sum_ii([2, 7, 11, 15], 9) -> [1, 2]
"""


def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []
