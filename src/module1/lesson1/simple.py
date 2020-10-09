# Training
# TODO: Вычислить сумму двух чисел
def amount(a, b):
    return a+b


# Training
# TODO: Вычислить разность двух чисел
def subtraction(a, b):
    return a-b


# Training
# TODO: Вычислить произведение двух чисел
def multiplication(a, b):
    return a*b


# Training
# TODO: Вычислить деление двух чисел
def division(a, b):
    return a/b


# Training
# TODO: Вычислить остаток от деления двух чисел
def mod(a, b):
    return a % b


# Training
# TODO: Вычислить целую часть от деления двух чисел
def integer_part(a, b):
    return a//b


# Trivial
# TODO: Вычислить дискриминант квадратного уравнения
def discriminant(a, b, c):
    discr = (b**2) - (4*a*c)
    return discr



# Trivial
# TODO: Поиск одного из корней квадратного уравнения
def sqrt(a, b, c):
    x = (-b + (discriminant(a, b, c) ** (1/2))) / (2*a)
    return x


# Trivial
# Пользователь задает время в часах, минутах и секундах, например, 8:20:35.
# TODO: Рассчитать время в секундах, прошедшее с начала суток (30035 в данном случае).
def seconds(hours, minutes, seconds):
    time_oclock = hours*3600 + minutes*60 + seconds
    return time_oclock


# Trivial
# Один человек может поднять вес до 10кг
# TODO: Посчитать количество человек, необходимое для переноски груза
# Примечание: для веса, который может поднять 1 человек, завести отдельную переменную
# Использовтаь операцию приведения типа int()
def peoples_for_work(weight):
    weight_for_one_people = 10
    peopless = int(weight / weight_for_one_people)
    return peopless


# Trivial
# На вход поступают два числа в виде строки
# TODO: Необходимо вывести сумму двух чисел
def string_amount(a, b):
    a = int(a)
    b = int(b)
    return a+b


# Easy
# TODO: Поменять местами первую и последнюю цифры четырехзначного числа
def swap(number):
    first_numb = str(number % 10)
    last_numb = str(number // 1000)
    midle_numb = str(number % 1000 // 10)
    res_numb = int(first_numb + midle_numb + last_numb)
    return res_numb


# Easy
# TODO: Вывести следущее четное число
def next_int(number):
    return (number // 2) * 2 + 2


# Easy
# Пользователь задает целое трехзначное число (например, 478).
# TODO: Необходимо вывести число, полученное из заданного перестановкой цифр в обратном порядке (например, 874).
def revert_number(number):
    first_numb = str(number % 10)
    last_numb = str(number // 100)
    midle_numb = str(number % 100 // 10)
    res_numb = int(first_numb + midle_numb + last_numb)
    return res_numb
