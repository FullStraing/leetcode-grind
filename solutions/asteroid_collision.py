"""
LeetCode 735. Asteroid Collision — Medium — Pattern: Stack

Asteroids move left (negative) or right (positive) along a line.
When two moving toward each other collide, the smaller one
explodes; equal sizes both explode; the survivor keeps moving and
may collide with the next asteroid.

Approach: simulate with a stack of surviving asteroids. A new
asteroid moving right is simply pushed. A new asteroid moving left
fights the stack top while the top moves right: the smaller explodes,
equal sizes both explode, and if the newcomer is smaller it is
destroyed. If the stack empties or the top also moves left, the
newcomer survives and is pushed.

Time:  O(n) — each asteroid is pushed and popped at most once
Space: O(n) — the survivors stack

Example:
    asteroid_collision([5, 10, -5]) -> [5, 10]
    asteroid_collision([8, -8]) -> []
    asteroid_collision([10, 2, -5]) -> [10]
    asteroid_collision([-2, -1, 1, 2]) -> [-2, -1, 1, 2]
"""


def asteroid_collision(asteroids: list[int]) -> list[int]:
    survivors: list[int] = []
    for rock in asteroids:
        alive = True
        while alive and rock < 0 and survivors and survivors[-1] > 0:
            top = survivors[-1]
            if top < -rock:
                survivors.pop()  # top explodes, newcomer keeps going
            elif top == -rock:
                survivors.pop()
                alive = False  # both explode
            else:
                alive = False  # newcomer explodes
        if alive:
            survivors.append(rock)
    return survivors
