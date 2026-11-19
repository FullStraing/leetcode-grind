"""
LeetCode 1047. Remove All Adjacent Duplicates In String — Easy — Pattern: Stack

Repeatedly delete adjacent duplicate characters until none remain.

Approach: one pass with a stack of kept characters. For each
character, if it equals the stack top, the pair cancels — pop the
top. Otherwise push the character. What remains is the fully
reduced string.

Time:  O(n) — one pass
Space: O(n) — the kept characters

Example:
    remove_duplicates("abbaca") -> "ca"
    remove_duplicates("azxxzy") -> "ay"
    remove_duplicates("aababaab") -> "ba"
"""


def remove_duplicates(s: str) -> str:
    kept: list[str] = []
    for ch in s:
        if kept and kept[-1] == ch:
            kept.pop()
        else:
            kept.append(ch)
    return "".join(kept)
