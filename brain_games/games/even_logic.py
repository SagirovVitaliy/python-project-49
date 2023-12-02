#!/usr/bin/env
from random import randint

from brain_games.games.games_logic import start_game


def main():
    start_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        _get_qustion_value
    )


def _get_qustion_value() -> tuple[str, str]:
    number = randint(0, 100)
    if number % 2 == 0:
        return str(number), "yes"
    return str(number), "no"
