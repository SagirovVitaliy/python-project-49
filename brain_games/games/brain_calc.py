#!/usr/bin/env
from random import choice, randint

from brain_games.scripts.question import start_game


def main():
    start_game(
        "What is the result of the expression?",
        _get_qustion_value
    )


def _get_qustion_value() -> tuple[str, str]:
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    expression = ["+", "-", "*"]
    result = f"{first_number} {choice(expression)} {second_number}"

    return result, str(eval(result))


if __name__ == '__main__':
    main()
