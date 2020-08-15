a = [[3, 7, 25],
     [14, 5, 4],
     [2, 17, 1]]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == max(a[i]):
            b = a[i][i]
            a[i][i] = a[i][j]
            a[i][j] = b
    print(a[i])
