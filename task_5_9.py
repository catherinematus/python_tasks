m = int(input('Введите m '))
n = int(input('Введите n '))
for i in range(m, n+1):
    c = ''
    for j in range(2, i):
        if i % j == 0:
            c += (str(j) + ' ')
    print(f'{i} : {c}')