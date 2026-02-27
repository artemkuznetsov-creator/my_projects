from math import sin, fabs, sqrt
a_0 = float(input('Введите а0'))
a_1 = float(input('Введите а1'))
a_2 = float(input('Введите а2'))
x = float(input('Введите х'))
terminal_ans = a_0 + a_1 * x + a_2*(fabs(sin(x)))**(1/3)
if x > 1 or x < -1:
    print('задан неверный х')
elif terminal_ans < 0:
    print('невозмжно вычислить значение корня')
else:
    answer = sqrt(terminal_ans)
    print(answer)

