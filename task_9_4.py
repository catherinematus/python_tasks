# Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный

def decorator(func):
    def reverse(*args):
        new_order = [args[-1 - i] for i in range(len(args))]
        result = func(*new_order)
        return result
    return  reverse

@decorator
def my_function(*args):
    print(*args)
    return args

my_function(1, 2, 5)
