import random
import numpy as np

a = int(input('Введите н: '))

def find_not_null(array):
    return [i for i, x in enumerate(array) if x !=0]
array1 = np.array([random.randint(0,1) for _ in range(20)])
print('1 задание: ')
print(find_not_null(array1))
print(array1)

matrix = np.eye(random.choice([i for i in range(1,a)]), dtype=float)
print('2 задание: ')
print(matrix)

def create_array():
    return np.random.randint(1,3, size=(a,a,a), dtype=int)
print('3 задание: ')
print(create_array())

print('4 задание: ')
print(np.zeros(a))

print('5 задание: ')
task5 = np.zeros((a,1), dtype=int)
if a >= 5:
    task5[4] = 1
print(task5)

print('6 задание: ')
m = int(input('Введите значение м: '))
print(np.arange(a,m+1))

print('7 задание: ')
normal = np.array([1,2,3,4,5,6,7])
reversed = np.flip(normal)
print(normal)
print(reversed)

print('8 задание: ')
border_matrix = np.ones((a, a), dtype=int)
border_matrix[1:-1, 1:-1] = 0
print(border_matrix)

print('9 задание: ')
under_diag_matrix = np.diag(np.arange(1, a), k=-1)
print(under_diag_matrix)

print('10 задание: ')
checkerboard = np.zeros((a, a), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print(checkerboard)

print('11 задание: ')
test_array = np.array([3, 7, 2, 9, 4, 9, 1])
print(f"Исходный: {test_array}")
test_array[test_array.argmax()] = 0
print(f"После замены: {test_array}")

print('12 задание: ')
target = float(input('Введите целевое значение: '))
search_array = np.array([1.5, 3.2, 4.8, 2.1, 5.6, 7.3])
nearest = search_array[np.argmin(np.abs(search_array - target))]
print(f"Массив: {search_array}")
print(f"Ближайшее к {target}: {nearest}")

print('13 задание: ')
shape_4d = (2, 3, 4, 5)
array_4d = np.random.randint(1, 10, shape_4d)
sum_last_two = np.sum(array_4d, axis=(-2, -1))
print(f"Форма 4D массива: {array_4d.shape}")
print(f"Сумма по последним двум осям, форма: {sum_last_two.shape}")
print(f"Результат (первые 2 элемента):\n{sum_last_two[0, 0]}")

print('14 задание: ')
matrix_2d = np.array([
    [1, 0, 3, 0],
    [4, 0, 6, 0],
    [7, 0, 9, 1]
])
print(f"Матрица:\n{matrix_2d}")
zero_columns = np.all(matrix_2d == 0, axis=0)
if np.any(zero_columns):
    print(f"Нулевые столбцы есть. Индексы: {np.where(zero_columns)[0]}")
else:
    print("Нулевых столбцов нет")

print('15 задание: ')
matrix_for_mean = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(f"Исходная матрица:\n{matrix_for_mean}")
row_means = matrix_for_mean.mean(axis=1, keepdims=True)
centered_matrix = matrix_for_mean - row_means
print(f"Матрица после вычитания среднего:\n{centered_matrix}")
print(f"Средние строк: {row_means.flatten()}")