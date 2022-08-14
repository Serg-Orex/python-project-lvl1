import random
from great_common_div import get_great_common_div


DISCRIPSION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question_game = (f'{first_number} {second_number}')
    correct_answer = get_great_common_div(first_number, second_number)
    return question_game, str(correct_answer)
