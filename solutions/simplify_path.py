"""
LeetCode 71. Simplify Path — Medium — Pattern: Stack

Given an absolute Unix path, simplify it: resolve '.' (stay) and
'..' (go up one level), collapse multiple slashes, drop trailing
slashes. The result is the canonical path.

Approach: split the path on '/', walk the parts with a stack of
directory names. Skip '' and '.'; '..' pops the stack if it is not
empty; anything else is a real directory name and is pushed. Join
the stack with '/' and a leading slash.

Time:  O(n) — one pass over the path
Space: O(n) — the directory stack

Example:
    simplify_path("/home/") -> "/home"
    simplify_path("/../") -> "/"
    simplify_path("/home//foo/./bar/../baz") -> "/home/foo/baz"
    simplify_path("/a/./b/../../c/") -> "/c"
"""


def simplify_path(path: str) -> str:
    stack: list[str] = []
    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)
