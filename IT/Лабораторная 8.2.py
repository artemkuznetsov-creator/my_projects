import random
def Matrix_change(matr=list):
    answer = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(matr[i][n-1-i])
            elif i + j == n-1:
                row.append(matr[i][i])
            else:
                row.append(matr[i][j])
        answer.append(row)
    return answer

n = int(input('Введи длину матрицы'))
data = [[random.randint(-50,50) for i in range(n)] for x in range(n)]
for line in data:
    print(line)

print('\n')

for line in Matrix_change(data):
    print(line)