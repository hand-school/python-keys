# Training
# TODO: Вычислить сумму двух чисел
def amount(a, b):
    x = a + b
    return x


# Training
# TODO: Вычислить разность двух чисел
def subtraction(a, b):
    return a - b


# Training
# TODO: Вычислить произведение двух чисел
def multiplication(a, b):
    result = a * b
    print(result)
    return result


# Training
# TODO: Вычислить деление двух чисел
def division(a, b):
    x = a / b
    print(x)
    return x


# Training
# TODO: Вычислить остаток от деления двух чисел
def mod(a, b):
    c = a % b
    x = int(input("напиши число"))
    print(c + x)
    return c


# Training
# TODO: Вычислить целую часть от деления двух чисел
def integer_part(a, b):
    x = a // b

    return x


# Trivial
# TODO: Вычислить дискриминант квадратного уравнения
def discriminant(a, b, c):
    x = b ** 2
    q = a * c
    return x - 4 * q


# Trivial
# TODO: Поиск одного из корней квадратного уравнения
def sqrt(a, b, c):
    pass


# Trivial
# Пользователь задает время в часах, минутах и секундах, например, 8:20:35.
# TODO: Рассчитать время в секундах, прошедшее с начала суток (30035 в данном случае).
def seconds(hours, minutes, seconds):
    a = hours * 60 * 60
    b = minutes * 60

    return a + b + seconds



# Trivial
# Один человек может поднять вес до 10кг
# TODO: Посчитать количество человек, необходимое для переноски груза
# Примечание: для веса, который может поднять 1 человек, завести отдельную переменную
# Использовтаь операцию приведения типа int()
def peoples_for_work(weight):
    a = 10
    b = weight / a
    b = int(b)
    return b



# Trivial
# На вход поступают два числа в виде строки
# TODO: Необходимо вывести число сумму двух чисел
def string_amount(a, b):
    a = int(a)
    b = int(b)
    result = amount(a, b)
    return result

# Easy
# TODO: Поменять местами первую и последнюю цифры числа
def swap(number):
    pass


# Easy
# Пользователь задает целое трехзначное число (например, 478).
# TODO: Необходимо вывести число, полученное из заданного перестановкой цифр в обратном порядке (например, 874).
def revert_number(number):
    pass


