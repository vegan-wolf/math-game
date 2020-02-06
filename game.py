from random import randint

print("Приветствуем Вас в нашей математической игре!")
number1 = randint(0, 100)
number2 = randint(0, 100)
print(str(number1) + ' + ' + str(number2) + ' = ' + '?' )
answer = int(input())
if answer == number1 + number2:
    print('Молодец!')
else:
    print('Попробуй ещё раз.')