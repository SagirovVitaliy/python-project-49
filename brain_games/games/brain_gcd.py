#!/usr/bin/env
from random import randint
from math import gcd

from brain_games.scripts.question import start_game


def main():
    start_game(
        "Find the greatest common divisor of given numbers.",
        _get_qustion_value
    )


def _get_qustion_value() -> tuple[str, str]:
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    result = f"{first_number} {second_number}"

    return result, str(gcd(first_number, second_number))


if __name__ == '__main__':
    main()
