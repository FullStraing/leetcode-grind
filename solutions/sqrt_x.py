"""
LeetCode 69. Sqrt(x) — Easy
Pattern: Binary Search

Given a non-negative integer `x`, return the square root of `x`
rounded down to the nearest integer, without using a built-in
exponent or power function.

Approach: binary search on the answer in [0, x]. If mid*mid is
exactly x, that is the answer; if it is smaller, the answer is at
or above mid; if larger, below mid. Track the largest mid whose
square is <= x.

Time:  O(log x)
Space: O(1)

Example:
    my_sqrt(4) -> 2
    my_sqrt(8) -> 2
    my_sqrt(0) -> 0
    my_sqrt(1) -> 1
"""


def my_sqrt(x: int) -> int:
    if x < 2:
        return x
    left, right, ans = 1, x // 2, 1
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == x:
            return mid
        if sq < x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
