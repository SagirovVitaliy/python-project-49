#!/usr/bin/env
from random import randint

from brain_games.scripts.question import start_game


def main():
    start_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        _get_qustion_value
    )


def _get_qustion_value() -> tuple[str, str]:
    number = randint(0, 100)
    if number <= 1:
        return str(number), "no"
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return str(number), "no"
    return str(number), "yes"


if __name__ == '__main__':
    main()
