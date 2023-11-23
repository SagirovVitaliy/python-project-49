import prompt
from typing import Callable


def start_game(
    greeting: str,
    qustion_value: Callable[..., tuple[str, str]]
) -> None:
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(greeting)

    _check_answer(name, qustion_value)


def _check_answer(
    name: str,
    qustion_value: Callable[..., tuple[str, str]]
) -> None:
    count_right_answer = 0

    while count_right_answer < 3:
        if not _get_question(name, qustion_value):
            return

        print("Correct!")
        count_right_answer += 1

    print(f"Congratulations, {name}!")


def _get_question(
    name: str,
    qustion_value: Callable[..., tuple[str, str]]
) -> bool:
    value = qustion_value()

    print(f"Question: {value[0]}")

    gamer_answer = prompt.string('Your answer: ')

    if value[1] == gamer_answer:
        return True

    _game_over(name, gamer_answer, value)
    return False


def _game_over(name: str, gamer_answer: str, value: tuple[str, str]) -> None:
    print(f"'{gamer_answer}' is wrong answer ;(. Correct answer was '{value[1]}'.") # noqa
    print(f"Let's try again, {name}!")
