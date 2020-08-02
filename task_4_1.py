a = [4, 9, 54, 8]
b = 0
while b < len(a):
    a[b] = a[b] * (-2)
    b += 1
print(a)

c = [4, 9, 54, 8]
d = []
for i in c:
    d.append(i * (-2))
print(d)
