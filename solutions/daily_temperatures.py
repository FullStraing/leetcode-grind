"""
LeetCode 739. Daily Temperatures — Medium — Pattern: Stack

Given daily temperatures, return for each day how many days you
have to wait until a warmer temperature; 0 if no warmer day comes.

Approach: monotonic decreasing stack of indices. Walk the days left
to right; while the current temperature is warmer than the day on
top of the stack, that day's wait is the distance between the two
indices — pop it and record the answer. Then push the current day.

Time:  O(n) — each index is pushed and popped at most once
Space: O(n) — the stack of indices

Example:
    daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) -> [1, 1, 4, 2, 1, 1, 0, 0]
    daily_temperatures([30, 40, 50, 60]) -> [1, 1, 1, 0]
    daily_temperatures([30, 60, 90]) -> [1, 1, 0]
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack: list[int] = []  # indices of days waiting for a warmer day
    for today, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            past = stack.pop()
            answer[past] = today - past
        stack.append(today)
    return answer
