""" Создать декоратор для функции, которая принимаем список чисел.
Декоратор будет удалять все четные элементы из списка"""

def only_odd(func):
    def delete_elen(list):
        list_new = [x for x in list if x % 2 != 0]
        result = func(list_new)
        return result
    return delete_elen

@only_odd
def my_list(numbers):
    print(numbers)
    return numbers

first_list = [1, 5, 8, 9, 10, 12]
my_list(first_list)

