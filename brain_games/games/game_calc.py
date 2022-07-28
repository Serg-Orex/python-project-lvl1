import random


DISCRIPSION = 'What is the result of the expression?'

st, fn = 1, 100

first_num = random.randint(st, fn)
second_num = random.randint(st, fn)

question_game = (f'{first_num} {random.choice(["+", "-", "*"])} {second_num}')
correct_answer = eval(question_game)
