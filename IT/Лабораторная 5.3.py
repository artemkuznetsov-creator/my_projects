from math import tan
for x in range(10*(-5), 10*5+1):
    number = x/10
    if number + 2 == 0:
        print('нет')
        continue
    else:
        print(tan(number)/((number + 2)**2))
