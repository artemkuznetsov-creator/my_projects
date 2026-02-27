user_list = [float(x) for x in input('Укажи элементы через пробел').split()]
minimal = 1000000000
for i in user_list:
    if i < minimal:
        minimal = i
print(minimal)
for x in range(len(user_list)):
    if user_list[x] == minimal:
        user_list[x] = 0
print(user_list)