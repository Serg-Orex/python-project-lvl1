import random


DISCRIPSION = 'Answer "yes" if the number is even, otherwise answer "no".'
question_game = random.randint(-1000, 1500)


def even_num(a):
    if a % 2 == 0:
        rezult = 'yes'
    else:
        rezult = 'no'
    return rezult


correct_answer = even_num(question_game)
