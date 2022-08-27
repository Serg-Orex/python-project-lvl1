import random
from brain_games.secondary_functions.is_prime import is_prime


DISCRIPSION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question_game = random.randint(1, 100)
    if is_prime(question_game) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_game, str(correct_answer)
