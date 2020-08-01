a = int(input('Сколько у вас будет гостей?\n'))
# Проверяем условие
if a > 50:
    print('Ресторан')
elif a >= 20 and a <= 50:
    print('Кафе')
else:
    print('Дом')