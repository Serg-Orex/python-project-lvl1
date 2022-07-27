import random


DISCRIPSION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
question = random.randint(-100, 200)


def prime_num(a):
    if a < 2:
        rezult = 'no'
    elif a == 2:
        rezult = 'yes'
    else:
        i = 2
        while i < a:
            if a % i == 0:
                rezult = 'no'
                break
            else:
                rezult = 'yes'
            i += 1
    return rezult


correct_answer = prime_num(question)
