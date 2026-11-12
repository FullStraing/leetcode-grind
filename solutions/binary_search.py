"""
LeetCode 704. Binary Search — Easy — Pattern: Binary Search

Given a sorted array `nums` and a `target`, return the target's index,
or -1 if it is not present. Must run in O(log n).

Approach: keep the candidate interval [lo, hi]. Compare the middle
element and discard the half that cannot contain the target.

Time:  O(log n) — the interval halves every step
Space: O(1)     — iterative, no recursion

Example:
    search([-1, 0, 3, 5, 9, 12], 9) -> 4
    search([-1, 0, 3, 5, 9, 12], 2) -> -1
"""


def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
