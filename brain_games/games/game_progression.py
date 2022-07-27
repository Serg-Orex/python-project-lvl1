import random

DISCRIPSION = 'What number is missing in the progression?'
a = random.randint(-100, 100)
lenght = random.randint(7, 10)
step = random.randint(0, 50)
ind = random.randint(0, (lenght - 1))
b = range(a, (a + lenght * step), step)

i = 0
s = [a]
while i < (lenght - 1):
    a += step
    s += [a]
    i += 1
correct_answer = s[ind]

s_1 = s
s_1[ind] = '..'
question = (" ".join(map(str, s_1)))
