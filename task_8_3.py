import math

def Sin1(x, e):
    result = 0
    while e > 0:
       y = (((-1) ** e) * (x ** (2 * e + 1))) / math.factorial(2 * e + 1)
       if abs(y) > e:
           result += y
           e -= 1
       else:
           e -= 1
    return result

x = 3

for e in range(1, 7):
    print(f'e= {e}, sin({x})= {Sin1(x, e)}')

