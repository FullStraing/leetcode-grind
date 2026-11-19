"""
LeetCode 155. Min Stack — Easy — Pattern: Stack

Design a stack that supports push, pop, top, and retrieving the
minimum element — all in constant time.

Approach: keep a second stack of minimums. Every push also pushes
the running minimum (min of the new value and the current minimum),
so the top of the min-stack is always the minimum of the whole
stack. Pop removes from both stacks.

Time:  O(1) for push / pop / top / get_min
Space: O(n) — the min-stack holds one entry per element

Example:
    s = MinStack()
    s.push(-2); s.push(0); s.push(-3)
    s.get_min() -> -3
    s.pop()
    s.top()     -> 0
    s.get_min() -> -2
"""


class MinStack:
    def __init__(self) -> None:
        self._values: list[int] = []
        self._mins: list[int] = []

    def push(self, val: int) -> None:
        self._values.append(val)
        if self._mins:
            self._mins.append(min(val, self._mins[-1]))
        else:
            self._mins.append(val)

    def pop(self) -> None:
        self._values.pop()
        self._mins.pop()

    def top(self) -> int:
        return self._values[-1]

    def get_min(self) -> int:
        return self._mins[-1]
