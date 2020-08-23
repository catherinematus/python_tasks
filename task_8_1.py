def double_factorial(n):
    factorial = 1
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            factorial *= i
        return  factorial
    else:
        for i in range(1, n+1, 2):
            factorial *= i
        return factorial

print(double_factorial(15))
print(double_factorial(14))
