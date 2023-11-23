from random import choice, randint
from brain_games.scripts.question import Game


class BrainCalc(Game):
    def get_qustion_value(self) -> tuple[str, str]:
        first_number = randint(0, 100)
        second_number = randint(0, 100)
        expression = ["+", "-", "*"]
        result = f"{first_number} {choice(expression)} {second_number}"

        return result, str(eval(result))


def main():
    BrainCalc().start_game(
        "What is the result of the expression?"
    )


if __name__ == '__main__':
    main()
