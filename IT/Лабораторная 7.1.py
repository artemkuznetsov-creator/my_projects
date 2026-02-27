import random
from string import ascii_letters
m = int(input("Введите длину списков: "))
list_1 = []
list_2 = []
d = {}
for i in range(m):
   list_1.append(random.choice(ascii_letters))
   list_2.append(random.choice(ascii_letters))
for x in range(len(list_1)):
    for y in range(len(list_2)):
        if x ==y:
            d[list_1[x]] = list_2[y]
print(list_1)
print(list_2)
print(d)

