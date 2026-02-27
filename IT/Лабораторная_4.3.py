x = float(input('Введите число x:'))
y = float(input('Введите число y:'))
if x > 0:
    x+=1
    y+=1
elif y>0:
    x+=1
    y+=1
else:
    x = abs(x)
    y = abs(y)
print(f'x = {x}')
print(f'y = {y}')