#!/usr/bin/env
from random import randint

from brain_games.games.games_logic import start_game


def main():
    start_game(
        "What number is missing in the progression?",
        _get_qustion_value
    )


def _get_qustion_value() -> tuple[str, str]:
    start = randint(0, 90)
    diff = randint(2, 9)
    replace_index = randint(0, 9)

    progression = _get_progression(start, diff)

    replaced_digit = _get_replaced_digit(progression, replace_index)

    _replace_digit(progression, replace_index)

    return " ".join(map(str, progression)), str(replaced_digit)


def _get_progression(start: int, diff: int) -> list:
    return [start + diff * i for i in range(10)]


def _get_replaced_digit(progression: list, replace_index: int) -> int:
    return progression[replace_index]


def _replace_digit(progression: list, replace_index: int) -> None:
    progression[replace_index] = ".."
