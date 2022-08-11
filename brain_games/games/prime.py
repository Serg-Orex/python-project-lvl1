import random


DISCRIPSION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question_game = random.randint(1, 100)
    if question_game < 2:
        correct_answer = 'no'
    elif question_game == 2:
        correct_answer = 'yes'
    else:
        i = 2
        while i < question_game:
            if question_game % i == 0:
                correct_answer = 'no'
                return question_game, str(correct_answer)
            else:
                correct_answer = 'yes'
            i += 1
    return question_game, str(correct_answer)
