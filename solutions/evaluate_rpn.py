"""
LeetCode 150. Evaluate Reverse Polish Notation — Medium — Pattern: Stack

Evaluate an arithmetic expression in Reverse Polish Notation:
tokens are integers or one of '+', '-', '*', '/'. Division truncates
toward zero (like C/Java, unlike Python's // on negatives).

Approach: scan tokens left to right with a stack of operands. A
number is pushed; an operator pops the top two operands, applies
the operator (left operand first), and pushes the result. The single
value left on the stack is the answer.

Time:  O(n) — one pass over the tokens
Space: O(n) — the operand stack

Example:
    eval_rpn(["2", "1", "+", "3", "*"]) -> 9
    eval_rpn(["4", "13", "5", "/", "+"]) -> 6
    eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) -> 22
"""


def eval_rpn(tokens: list[str]) -> int:
    stack: list[int] = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                # int() truncates toward zero, unlike // on negatives.
                stack.append(int(left / right))
        else:
            stack.append(int(token))
    return stack[0]
