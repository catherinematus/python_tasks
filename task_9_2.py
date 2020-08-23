""" Создаем lambda функциюб которая принимает на вход неопределённое количество именных аргументов
 и выводит словарь с ключами удвоенной длины"""

double_key = lambda **kwargs: {key * 2: value for key, value in kwargs.items()}
print(double_key(length = 2, weigth = 3))
