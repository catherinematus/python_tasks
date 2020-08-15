array = [1, 3, 7, 13, 6, 34, 65, 6, 23, 45, 876, 4, 13, 14, 15, 16, 17, 18, 19]
b = max(array)
i = 0
while i < len(array):
    if array[i] % 2 == 0:
        array[i] = b
    i += 1
print(array)
