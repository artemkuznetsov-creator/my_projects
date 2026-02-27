import random
n = int(input('Введите длину массива '))
user_list = [random.randint(1,5) for x in range(n)]
minimal = 1000000000
for i in user_list:
    if i < minimal:
        minimal = i
print(minimal)
for x in range(len(user_list)):
    if user_list[x] == minimal:
        user_list[x] = 0
print(user_list)