#!/usr/bin/env
from random import choice, randint

from brain_games.games.games_logic import start_game


def main():
    start_game(
        "What is the result of the expression?",
        _get_qustion_value
    )


def _get_qustion_value() -> tuple[str, str]:
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    expression = ["+", "-", "*"]

    choice_expression = choice(expression)

    result = f"{first_number} {choice_expression} {second_number}"

    if choice_expression == "+":
        return result, str(first_number + second_number)

    if choice_expression == "-":
        return result, str(first_number - second_number)

    if choice_expression == "*":
        return result, str(first_number * second_number)
