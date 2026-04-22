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








