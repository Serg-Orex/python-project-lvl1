import prompt


def get_game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.DISCRIPSION}')
    game_rounds_count = 3
    for i in range(game_rounds_count):
        question_game, correct_answer = game.get_question_and_answer()
        print(f'Question: {question_game}')
        user_answer = input('Your answer: ')
        if user_answer != correct_answer:
            return print(f"'{user_answer}' is wrong answer ;(."
                         f" Correct answer was '{correct_answer}'.\n"
                         f"Let's try again, {name}!")
            return print('Correct!')
    print(f'Congratulations, {name}!')
