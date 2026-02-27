import random
m = int(input("Количество строк: "))
n = int(input("Количество столбцов: "))
matr = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(-20,20))
    matr.append(row)
print(matr)
answer = []
for i in range(m):
    s = 0
    for j in range(n):
        if matr[i][j] > 0:
            s += matr[i][j]
    answer.append(s)
print(answer)


