"""
LeetCode 209. Minimum Size Subarray Sum — Medium
Pattern: Sliding Window

Given an array of positive integers `nums` and a target sum, find the
minimal length of a contiguous subarray whose sum is at least `target`.
Return 0 if no such subarray exists.

Approach: sliding window with a running sum. Expand the right edge
until the sum reaches the target, then shrink from the left while the
sum stays at or above the target, recording the shortest window seen.
All numbers are positive, so shrinking never increases the sum.

Time:  O(n)   — each element enters and leaves the window once
Space: O(1)

Example:
    min_sub_array_len(7, [2, 3, 1, 2, 4, 3]) -> 2   ([4, 3])
    min_sub_array_len(4, [1, 4, 4])           -> 1   ([4])
    min_sub_array_len(11, [1, 1, 1, 1, 1])    -> 0
"""


def min_sub_array_len(target: int, nums: list[int]) -> int:
    best = len(nums) + 1
    total = 0
    left = 0
    for right, num in enumerate(nums):
        total += num
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == len(nums) + 1 else best
