#!/usr/bin/env
from random import randint
from brain_games.scripts.question import Game


class BrainEven(Game):
    def get_qustion_value(self) -> tuple[str, str]:
        number = randint(0, 100)
        if number % 2 == 0:
            return str(number), "yes"
        return str(number), "no"


def main():
    BrainEven().start_game(
        'Answer "yes" if the number is even, otherwise answer "no".'
    )


if __name__ == '__main__':
    main()
