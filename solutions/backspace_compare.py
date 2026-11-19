"""
LeetCode 844. Backspace String Compare — Easy — Pattern: Stack

'#' is a backspace: it deletes the previous character. Return
whether two strings become equal after applying all backspaces.

Approach: build each string's final form with a stack — push
letters, pop on '#'. Then compare the two results. (A two-pointer
variant does it in O(1) space, but the stack version is the direct
read of the problem.)

Time:  O(n + m) — one pass over each string
Space: O(n + m) — the two reduced strings

Example:
    backspace_compare("ab#c", "ad#c") -> True   # both become "ac"
    backspace_compare("ab##", "c#d#") -> True   # both become ""
    backspace_compare("a#c", "b") -> False      # "c" vs "b"
"""


def _apply_backspaces(s: str) -> str:
    kept: list[str] = []
    for ch in s:
        if ch == "#":
            if kept:
                kept.pop()
        else:
            kept.append(ch)
    return "".join(kept)


def backspace_compare(s: str, t: str) -> bool:
    return _apply_backspaces(s) == _apply_backspaces(t)
