import random
from brain_games.libs.is_prime import is_prime


DISCRIPSION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question_game = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question_game) is True else 'no'
    return question_game, str(correct_answer)
