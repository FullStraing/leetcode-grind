"""
LeetCode 11. Container With Most Water — Medium
Pattern: Two Pointers

Given an array `height` where each element is the height of a vertical
line, find the two lines that, together with the x-axis, form a
container holding the most water.

Approach: two pointers at both ends. The area is limited by the
shorter line, so move the pointer at the shorter line inward — only
that move can possibly find a taller line and a bigger area. Track
the largest area seen.

Time:  O(n)   — each pointer moves at most n steps
Space: O(1)

Example:
    max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49
    max_area([1, 1])                       -> 1
    max_area([4, 3, 2, 1, 4])              -> 16
"""


def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        if height[left] < height[right]:
            best = max(best, width * height[left])
            left += 1
        else:
            best = max(best, width * height[right])
            right -= 1
    return best
