import random


def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'''Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no".''')

    i = 0
    while i < 3:
        num = random.randint(-1000, 1500)
        print(f'Question: {num}')
        answ = input('Your answer: ')
        if num % 2 == 0:
            if answ == 'yes':
                print('Correct!')
                i += 1
            else:
                print(''''no' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!''')
                exit()
        else:
            if answ == 'no':
                print('Correct!')
                i += 1
            else:
                print(f''''yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!''')
                exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
