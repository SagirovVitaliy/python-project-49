import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_right_answer = 0

    while count_right_answer < 3:
        if not _get_question(name):
            return

        print("Correct!")
        count_right_answer += 1

    print(f"Congratulations, {name}!")


def _get_question(name: str) -> bool:
    number = randint(0, 100)

    print(f"Question: {number}")

    our_answer = _check_number(number)

    gamer_answer = prompt.string('Your answer: ')

    if our_answer == gamer_answer:
        return True

    print(f"'{gamer_answer}' is wrong answer ;(. Correct answer was '{our_answer}'.") # noqa
    print(f"Let's try again, {name}!")
    return False


def _check_number(number: int) -> str:
    if number % 2 == 0:
        return "yes"
    return "no"


if __name__ == '__main__':
    main()
