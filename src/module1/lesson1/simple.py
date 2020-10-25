# Training
# TODO: Вычислить сумму двух чисел
def amount(a, b):
    return sum([a, b])


# Training
# TODO: Вычислить разность двух чисел
def subtraction(a, b):
    return a - b


# Training
# TODO: Вычислить произведение двух чисел
def multiplication(a, b):
    return a * b


# Training
# TODO: Вычислить деление двух чисел
def division(a, b):
    return a / b


# Training
# TODO: Вычислить остаток от деления двух чисел
def mod(a, b):
    return a % b


# Training
# TODO: Вычислить целую часть от деления двух чисел
def integer_part(a, b):
    return a // b


# Trivial
# TODO: Вычислить дискриминант квадратного уравнения
def discriminant(a, b, c):
    d = (b ** 2) - 4 * a * c
    return d


# Trivial
# TODO: Поиск одного из корней квадратного уравнения
def sqrt(a, b, c):
    pass


# Trivial
# Пользователь задает время в часах, минутах и секундах, например, 8:20:35.
# TODO: Рассчитать время в секундах, прошедшее с начала суток (30035 в данном случае).
def seconds(hours, minutes, seconds):
    time_in_sec = ((hours * 60) * 60) + (minutes * 60) + seconds
    return time_in_sec



# Trivial
# Один человек может поднять вес до 10кг
# TODO: Посчитать количество человек, необходимое для переноски груза
# Примечание: для веса, который может поднять 1 человек, завести отдельную переменную
# Использовтаь операцию приведения типа int()
def peoples_for_work(weight):
    one = 10
    peoples = weight // 10
    return peoples


# Trivial
# На вход поступают два числа в виде строки
# TODO: Необходимо вывести сумму двух чисел
def string_amount(a, b):
    return a + b


# Easy
# TODO: Поменять местами первую и последнюю цифры четырехзначного числа
def swap(number):
    first = number // 1000
    last = number % 10
    mid = (number % 1000) // 10
    return (last * 1000) + mid * 10 + first


# Easy
# TODO: Вывести следущее четное число
def next_int(number):
    return number + 2


# Easy
# Пользователь задает целое трехзначное число (например, 478).
# TODO: Необходимо вывести число, полученное из заданного перестановкой цифр в обратном порядке (например, 874).
def revert_number(number):
    pass
