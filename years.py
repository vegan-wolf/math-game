old = int(input ('Сколько тебе лет?'))
if old < 3:
    print('Привет малыш!')
elif old > 3 and old < 6 :
    print("Привет дошкольник!")
elif old > 6 and old < 17 :
    print("Привет ученик!")
elif old > 17 and old < 60:
    print('Привет дядя!')
else:
    print("привет старик")