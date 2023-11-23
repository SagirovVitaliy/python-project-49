import prompt


class Game:
    def start_game(self, greeting: str) -> None:
        print("Welcome to the Brain Games!")
        name = prompt.string('May I have your name? ')
        print(f"Hello, {name}!")
        print(greeting)

        self._check_answer(name)

    def _check_answer(self, name: str) -> None:
        count_right_answer = 0

        while count_right_answer < 3:
            if not self._get_question(name):
                return

            print("Correct!")
            count_right_answer += 1

        print(f"Congratulations, {name}!")

    def _get_question(self, name: str) -> bool:
        value = self.get_qustion_value()

        print(f"Question: {value[0]}")

        gamer_answer = prompt.string('Your answer: ')

        if value[1] == gamer_answer:
            return True

        self._game_over(name, gamer_answer, value)
        return False

    def _game_over(
            self, name: str, gamer_answer: str, value: tuple[str, str]
    ) -> None:
        print(f"'{gamer_answer}' is wrong answer ;(. Correct answer was '{value[1]}'.") # noqa
        print(f"Let's try again, {name}!")

    def get_qustion_value(self) -> tuple[str, str]:
        "Должна быть переопределена"
        raise NotImplementedError
