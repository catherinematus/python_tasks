from itertools import groupby

a = [1, 6, 3, 6, 7, 8, 3, 2, 1, 8, 9, 10, 1, 12, 134, 135, 4, 7, 8]
n = ''
for i in range(1, len(a)):
    if a[i-1] < a[i]:
        n += '+'
    else:
        n += '-'
g = groupby(n)
up = [k for k, v in g if k == '+']
print(len(up))
