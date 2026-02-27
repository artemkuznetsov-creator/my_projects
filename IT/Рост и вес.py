height = int(input('Введите рост: '))
weight = int(input('Введите вес: '))
x = height - weight
if x > 50:
    print('Вам надо поправиться')
elif x < 100:
    print('Вам надо похудеть')
else:
    print('У вас нормальная масса тела')