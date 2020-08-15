while True:
    form = input()
    x = int(form[0])
    sign = form[1]
    y = int(form[2])
    if sign == '+':
        z = x + y
        print(z)
    elif sign == '-':
        z = x - y
        print(z)
    elif sign == '*':
        z = x * y
        print(z)
    elif sign == '/' and y != 0:
        z = x/y
        print(z)
    elif sign == '/' and y == 0:
        print('Деление на ноль не возможно')
    elif sign == '0':
        break
    else:
        print('Проверте правильность введенных данных')

