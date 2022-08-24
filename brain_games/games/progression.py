import random


DISCRIPSION = 'What number is missing in the progression?'

def get_question_and_answer():
    start = random.randint(-100, 100)
    length = random.randint(7, 10)
    step = random.randint(1, 50)
    hidden_index = random.randint(0, (length - 1))
    progression = list(range(start, (start + length * step), step))
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question_game = " ".join(map(str, progression))
    return question_game, str(correct_answer)
