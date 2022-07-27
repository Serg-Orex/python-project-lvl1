import random

DISCRIPSION = 'Find the greatest common divisor of given numbers.'

st, fn = 1, 100

a = random.randint(st, fn)
b = random.randint(st, fn)
question = (f'{a} {b}')


def great_common_div(a, b):
    if a > b:
        c = b
    else:
        c = a
    d = 1
    while d <= c:
        if b % d == 0 and a % d == 0:
            gcd = d
            d += 1
        else:
            d += 1
    return gcd


correct_answer = great_common_div(a, b)
