import prompt


def get_game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
{game.DISCRIPSION}''')
    number_of_game_rounds = 3
    for i in range(number_of_game_rounds):
        question_game, correct_answer = game.get_question_and_answer()
        print(f'Question: {question_game}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            return print(f"'{user_answer}' is wrong answer ;(."
                         f" Correct answer was '{correct_answer}'.\n"
                         f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
