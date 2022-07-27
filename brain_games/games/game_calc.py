import random

DISCRIPSION = 'What is the result of the expression?'

st, fn = 1, 100

a = random.randint(st, fn)
b = random.randint(st, fn)
question = (f'{a} {random.choice(["+", "-", "*"])} {b}')
correct_answer = eval(question)
