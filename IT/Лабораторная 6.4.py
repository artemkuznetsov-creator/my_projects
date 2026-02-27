import random
n = int(input('Введите размер массивва: '))
user_list = [random.randint(1,50) for x in range(n)]
print(user_list)
answer = 0
с = 1
for element in range(len(user_list)-1):
    if user_list[element-1] < user_list[element] > user_list[element+1]:
        answer = с
    с += 1
print(answer)