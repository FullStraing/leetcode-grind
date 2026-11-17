"""
LeetCode 278. First Bad Version — Easy
Pattern: Binary Search

Versions 1..n are good up to some point, then all bad. Given an API
`is_bad_version(version)` (passed in as a callable), find the first
bad version while minimising API calls.

Approach: binary search on the answer. If the middle version is bad,
the first bad version is at or before it; if it is good, the first
bad version is after it. The loop ends with `left` at the first bad
version.

Time:  O(log n) API calls
Space: O(1)

Example:
    first_bad_version(5, lambda v: v >= 4) -> 4
    first_bad_version(1, lambda v: True)   -> 1
    first_bad_version(3, lambda v: v >= 3) -> 3
"""


def first_bad_version(n: int, is_bad_version) -> int:
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left
