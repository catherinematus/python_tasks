a = int(input('a = '))
b = int(input('b = '))
n = int(input('n = '))
m = int(input('m = '))
from random import randint
matrix = [[randint(a, b) for j in range(n)] for i in range(m)]
print(matrix)
