for n in range(200, 300):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum > n:
        result = 0
        for j in range(1, sum):
            if sum % j == 0:
                result += j
        if result == n:
            print(n, sum)