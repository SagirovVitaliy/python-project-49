#!/usr/bin/env
from random import randint

from brain_games.scripts.question import start_game


def main():
    start_game(
        "What number is missing in the progression?",
        _get_qustion_value
    )


def _get_qustion_value() -> tuple[str, str]:
    start = randint(0, 90)
    diff = randint(2, 9)
    replace_index = randint(0, 9)
    progression = [start + diff * i for i in range(10)]
    replaced_digit = progression[replace_index]
    progression[replace_index] = ".."

    return " ".join(map(str, progression)), str(replaced_digit)


if __name__ == '__main__':
    main()
