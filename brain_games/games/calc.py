import random


DISCRIPSION = 'What is the result of the expression?'

def get_question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    math_operator = random.choice(["+", "-", "*"])
    question_game = (f'{first_number} {math_operator} {second_number}')
    if math_operator == '+':
        correct_answer = first_number + second_number
    elif math_operator == '-':
        correct_answer = first_number - second_number
    elif math_operator == '*':
        correct_answer = first_number * second_number
    return question_game, str(correct_answer)
