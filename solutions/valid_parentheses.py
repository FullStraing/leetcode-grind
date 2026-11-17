"""
LeetCode 20. Valid Parentheses — Easy
Pattern: Stack

Given a string `s` containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid: open brackets
must be closed by the same type of brackets, and in the correct order.

Approach: scan left to right with a stack. Push every opening bracket.
On a closing bracket, the top of the stack must be the matching opener
— pop it; otherwise the string is invalid. At the end the stack must
be empty (every opener was closed).

Time:  O(n)   — one pass over the string
Space: O(n)   — the stack holds at most all openers

Example:
    is_valid("()[]{}") -> True
    is_valid("(]")     -> False
    is_valid("([)]")   -> False
    is_valid("{[]}")   -> True
"""


def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack
