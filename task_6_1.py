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

# Находим номер строки с максимальной суммой элементов
array_sum = []
for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
    array_sum.append(sum)
print('Номер строки с максимальной суммой элементов ' + str(array_sum.index(max(array_sum))+1))

# Находим индекс колонки с максимальной суммой элементов
array_sum_1 = []
for i in range(n):
    s = 0
    for j in range(m):
        s += int(matrix[j][i])
    array_sum_1.append(s)
print('Номер столбца с максимальной суммой элеметов ' + str(array_sum_1.index(max(array_sum_1)) + 1))

