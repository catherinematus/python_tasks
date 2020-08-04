n = 15
a = b = 1
c = 0
d = [a]
while c < n - 1:
    d.append(b)
    sum = a + b
    a = b
    b = sum
    c += 1
print(d)

a = b = 1
d = [a]
for i in range(n-1):
    d.append(b)
    sum = a + b
    a = b
    b = sum
print(d)

