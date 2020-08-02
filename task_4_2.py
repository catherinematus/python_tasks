a = [5, 8, 2, -5, 67, 13, 14, 122, 4, 128, 3]
b = 0
c = 0
while b < len(a):
    if a[b] % 2 == 0:
        c += 1
    b += 1
print(c)

d = 0
for i in a:
    if i % 2 == 0:
       d += 1
print(d)
