"""
LeetCode 35. Search Insert Position — Easy
Pattern: Binary Search

Given a sorted array of distinct integers `nums` and a `target`,
return the index if the target is found; otherwise return the index
where it would be inserted to keep the array sorted.

Approach: binary search. The loop invariant is that the answer lies
in [left, right]; when the loop ends, `left` is the first index whose
value is >= target — exactly the insertion point.

Time:  O(log n)
Space: O(1)

Example:
    search_insert([1, 3, 5, 6], 5) -> 2
    search_insert([1, 3, 5, 6], 2) -> 1
    search_insert([1, 3, 5, 6], 7) -> 4
    search_insert([1, 3, 5, 6], 0) -> 0
"""


def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
