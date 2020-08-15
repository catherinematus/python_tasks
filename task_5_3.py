for d in range(200, 300):
    sum = 0
    for i in range(1, d):
        if d % i == 0:
            sum += i
    if sum > d:
        result = 0
        for j in range(1, sum):
            if sum % j == 0:
                result += j
        if result == d:
            print(d, sum)
