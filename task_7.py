def inch_to_cm(x):
    y = x * 2.54
    return y

def cm_to_inch(x):
    y = x / 2.54
    return y

def mile_to_km(x):
    y = x * 1.61
    return y

def km_to_mile(x):
    y = x / 1.61
    return y

def lb_to_kg(x):
    y = x * 0.45
    return y

def kg_to_lb(x):
    y = x / 0.45
    return y

def ounce_to_gr(x):
    y = x * 28.35
    return y

def gr_to_ounce(x):
    y = x / 28.35
    return y

def gallon_to_litr(x):
    y = x * 3.79
    return y

def litr_to_gallon(x):
    y = x / 3.79
    return y

def pint_to_gr(x):
    y = x * 0.57
    return y

def gr_to_pint(x):
    y = x / 0.57
    return y

while True:
    n = int(input('Введите число от 1 до 12\n'))
    if n == 1:
        x = float(input())
        print(inch_to_cm(x))
    elif n == 2:
        x = float(input())
        print(cm_to_inch(x))
    elif n == 3:
        x = float(input())
        print(mile_to_km(x))
    elif n == 4:
        x = float(input())
        print(km_to_mile(x))
    elif n == 5:
        x = float(input())
        print(lb_to_kg(x))
    elif n == 6:
        x = float(input())
        print(kg_to_lb(x))
    elif n == 7:
        x = float(input())
        print(ounce_to_gr(x))
    elif n == 8:
        x = float(input())
        print(gr_to_ounce(x))
    elif n == 9:
        x = float(input())
        print(gallon_to_litr(x))
    elif n == 10:
        x = float(input())
        print(litr_to_gallon(x))
    elif n == 11:
        x = float(input())
        print(pint_to_gr(x))
    elif n == 12:
        x = float(input())
        print(gr_to_pint(x))
    elif n == 0:
        break
    else:
        print('Введите правильное число')

