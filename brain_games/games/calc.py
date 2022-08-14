import random


DISCRIPSION = 'What is the result of the expression?'


def get_question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question_game = (f'{first_number} {random.choice(["+", "-", "*"])}'
                     f' {second_number}')
    correct_answer = eval(question_game)
    return question_game, str(correct_answer)
