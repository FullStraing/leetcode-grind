"""
LeetCode 125. Valid Palindrome — Easy
Pattern: Two Pointers

Given a string `s`, return true if it is a palindrome after converting
all uppercase letters to lowercase and removing all non-alphanumeric
characters.

Approach: two pointers starting at both ends, skipping characters that
are not alphanumeric, and comparing the remaining characters
case-insensitively. The pointers move toward each other and stop as
soon as a mismatch is found.

Time:  O(n)   — each character visited at most once
Space: O(1)   — no extra string is built

Example:
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("race a car")                     -> False
    is_palindrome(" ")                              -> True
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
