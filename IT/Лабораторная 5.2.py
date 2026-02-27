from math import factorial
x = int(input('Введите значение х: '))
n = int(input('Введите значение n: '))
s = 0
for i in range(1,n+1):
    s += 1/(factorial(i)) + (abs(x)**0.5)
print("Сумма = ", s)
