import random


DISCRIPSION = 'What number is missing in the progression?'
start_progression = random.randint(-100, 100)
lenght = random.randint(7, 10)
step_progression = random.randint(0, 50)
ind = random.randint(0, (lenght - 1))


i = 0
progression = [start_progression]
while i < (lenght - 1):
    start_progression += step_progression
    progression += [start_progression]
    i += 1
correct_answer = progression[ind]

progression[ind] = '..'
question_game = (" ".join(map(str, progression)))
