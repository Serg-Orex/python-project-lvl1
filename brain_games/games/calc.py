import random
import operator


DISCRIPSION = 'What is the result of the expression?'


def get_question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operations = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    )
    operator_name, operator_method = random.choice(operations)
    question_game = (f'{first_number} {operator_name} {second_number}')
    correct_answer = operator_method(first_number, second_number)
    return question_game, str(correct_answer)
