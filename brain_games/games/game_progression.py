"""Main module of game brain-progression."""

import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(first_num, diff_progression, length_progression):
    """Generate progression.

    Args:
        first_num: int
        diff_progression: int
        length_progression: int

    Returns:
        Return progression.
    """
    progression = []
    index = 0
    while index < length_progression:
        progression.append(str(first_num + diff_progression * index))
        index += 1
    return progression


def generate_round():
    """Ask question and push true answer.

    Returns:
        Return rules of the game,
        question to player,
        true answer.
    """
    first_num = random.randint(1, 100)  # noqa: S311
    diff_progression = random.randint(1, 10)  # noqa: S311
    length_progression = 10
    miss_number = random.randint(0, 9)  # noqa: S311
    progression = generate_progression(
        first_num, diff_progression, length_progression)
    true_answer = progression.pop(miss_number)
    progression.insert(miss_number, '..')
    return ' '.join(progression), true_answer
