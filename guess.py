import random

number = random.randint(0, 20)
guess = int(input('Я загадал число. Угадай его! '))
while guess != number:
    if guess < number:
        print('Твоя догадка меньше загадонного числа...')
    else:
        print('Твоё число больше...')
    guess = int(input('Попробуй ещё раз... '))
print('Поздравляю вы угадали!!!')
