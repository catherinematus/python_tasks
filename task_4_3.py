dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Создаем список из ключей словаря
a = list(dictionary.keys())
# Создаем список из зачений словаря
c = list(dictionary.values())
b = 0
# Перебираем элементы списка и каждому элементу(тип строка) добавляем его длину, преобразуя цифру в число
while b < len(a):
    a[b] += str(len(a[b]))
    b += 1
# Выводим новый словарь, соединяя два списка
print(dict(zip(a, c)))

dictionary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
a = list(dictionary.keys())
c = list(dictionary.values())
# Задаем пустой список
d = []
for i in a:
    i += str(len(i))
    # Добавляем новые элементы в список d
    d.append(i)
print(dict(zip(d, c)))
