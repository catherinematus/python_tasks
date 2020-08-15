b = input('Введите число ')
sum = 0
mpl = 1
for i in range(len(b)):
    sum += int(b[i])
    mpl = mpl * int(b[i])
print('Сумма цифр числа = ' + str(sum))
print('Произведение цифр числа = ' + str(mpl))
