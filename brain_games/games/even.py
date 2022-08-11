import random


DISCRIPSION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question_game = random.randint(-1000, 1500)
    if question_game % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_game, str(correct_answer)
