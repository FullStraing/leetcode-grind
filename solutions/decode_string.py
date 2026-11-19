"""
LeetCode 394. Decode String — Medium — Pattern: Stack

Decode strings like "3[a2[c]]" -> "accaccacc": a number k followed
by a bracketed string means that string repeated k times, with
nesting allowed.

Approach: one pass with two stacks — counts and the strings built
so far. On a digit, build the repeat count. On '[', push the current
count and the current string, then start fresh. On ']', pop a count
and the previous string and append the current string repeated that
many times. Plain letters are appended to the current string.

Time:  O(n) in the length of the decoded output
Space: O(n) — the stacks, depth = nesting level

Example:
    decode_string("3[a]2[bc]") -> "aaabcbc"
    decode_string("3[a2[c]]") -> "accaccacc"
    decode_string("2[abc]3[cd]ef") -> "abcabccdcdcdef"
"""


def decode_string(s: str) -> str:
    counts: list[int] = []
    strings: list[str] = []
    current = ""
    k = 0
    for ch in s:
        if ch.isdigit():
            k = k * 10 + int(ch)
        elif ch == "[":
            counts.append(k)
            strings.append(current)
            current = ""
            k = 0
        elif ch == "]":
            current = strings.pop() + current * counts.pop()
        else:
            current += ch
    return current
