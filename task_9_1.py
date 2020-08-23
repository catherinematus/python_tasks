"""Отформатировать строки в формате {i} - {string}, i - порядковый номер строки в списке.
Используем генератор списков"""

list = ['hello friends',
        'how are you?',
        'it\'s very interesting']
new_list = [f'{i + 1} - {list[i]}' for i in range(len(list))]
print(new_list)