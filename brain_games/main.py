import importlib
import prompt
import brain_games.games.game_even as game


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
{game.DISCRIPSION}''')

    i = 0
    while i < 3:
        print(f'Question: {game.question_game}')
        user_answer = input('Your answer: ')
        if user_answer == str(game.correct_answer):
            print('Correct!')
            i += 1
            importlib.reload(game)
        else:
            st = "'" + user_answer + "' is wrong answer ;(."
            st = st + "Correct answer was '" + str(game.correct_answer) + "'."
            print(st)
            print(f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game_engine(game)
