a = [3, 5, 7, 10, 1, 2, 3]
b = 0
c = []
while b < len(a):
    c.append(a[b - 1])
    b += 1
print(c)

a = [3, 5, 7, 10, 1, 2, 3]
c = []
for i in range(len(a)):
    c.append(a[i-1])
print(c)
