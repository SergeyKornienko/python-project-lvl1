"""Main module of game brain-calc."""

import operator
import random

DESCRIPTION = 'What is the result of the expression?'


def generate_expression():
    """Generate expression.

    Returns:
        Return two operands,
        operation.
    """
    return (random.randint(0, 20),  # noqa: S311
            random.randint(0, 20),  # noqa: S311
            random.choice(['+', '-', '*']),  # noqa: S311
            )


def generate_round():
    """Ask question and make calculation.

    Returns:
        Return question to player,
        true answer.
    """
    (operand1, operand2, operation) = generate_expression()
    question = '{a} {b} {c}'.format(a=operand1, b=operation, c=operand2)
    if operation == '+':
        answer = operator.add(operand1, operand2)
    elif operation == '-':
        answer = operator.sub(operand1, operand2)
    elif operation == '*':
        answer = operator.mul(operand1, operand2)
    return question, str(answer)
