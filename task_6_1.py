a = int(input('a = '))
b = int(input('b = '))
n = int(input('n = '))
m = int(input('m = '))

# Вводим матрицу случайных чисел с количеством столбцов n и строк m
from random import randint

matrix = [[randint(a, b) for j in range(n)] for i in range(m)]
print(matrix)

# Находим максимальный элемент матрицы
new_array1 = []
for i in matrix:
    max_i = max(i)
    new_array1.append(max_i)
print('Максимальный элемент матрицы ' + str(max(new_array1)))

# Находим минимальный элемент матрицы
new_array2 = []
for i in matrix:
    min_i = min(i)
    new_array2.append(min_i)
print('Минимальный элемент матрицы ' + str(min(new_array2)))

# Находим сумму всех элементов матрицы
sum = 0
for i in matrix:
    for j in i:
        sum += j
print('Сумма всех элементов матрицы ' + str(sum))

# Находим индекс строки с максимальной суммой элементов
array_sum = []
for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
    array_sum.append(sum)
print('Индекс строки с максимальной суммой элементов ' + str(array_sum.index(max(array_sum))))

# Находим индекс столбца с максимальной суммой элементов
array_sum_1 = []
for i in range(n):
    s = 0
    for j in range(m):
        s += int(matrix[j][i])
    array_sum_1.append(s)
print('Индекс столбца с максимальной суммой элеметов ' + str(array_sum_1.index(max(array_sum_1))))

# Находим индекс строки с минимальной суммой элементов
print('Индекс строки с минимальной суммой элементов ' + str(array_sum.index(min(array_sum))))

# Находим индекс столбца с минимальной суммой элементов
print('Индекс столбца с минимальной суммой элеметов ' + str(array_sum_1.index(min(array_sum_1))))

import copy
matrix_top = copy.deepcopy(matrix)
# Обнуляем все элементы выше главной диагонали
for i in range(n):
    for j in range(i + 1, n):
        matrix_top[i][j] = 0
print(matrix_top)
matrix_down = copy.deepcopy(matrix)
# Обнуляем все элементы выше главной диагонали
for i in range(n):
    for j in range(0, i):
        matrix_down[i][j] = 0
print(matrix_down)
