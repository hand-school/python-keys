# Training
# TODO: Вычислить сумму двух чисел
def amount(a, b):
    return a + b


# Training
# TODO: Вычислить разность двух чисел
def subtraction(a, b):
    c = a - b
    return c


# Training
# TODO: Вычислить произведение двух чисел
def multiplication(a, b):
    c = a*b
    return c


# Training
# TODO: Вычислить деление двух чисел
def division(a, b):
    c = a/b
    return c


# Training
# TODO: Вычислить остаток от деления двух чисел
def mod(a, b):
    c = a % b
    return c


# Training
# TODO: Вычислить целую часть от деления двух чисел
def integer_part(a, b):
    c = a // b
    return c


# Trivial
# TODO: Вычислить дискриминант квадратного уравнения
def discriminant(a, b, c):
    c = b**2 - (4*a*c)
    return c


# Trivial
# TODO: Поиск одного из корней квадратного уравнения
def sqrt(a, b, c):
    c = (-b + (discriminant(a, b, c))**1/2)/2*a
    return c

# Trivial
# Пользователь задает время в часах, минутах и секундах, например, 8:20:35.
# TODO: Рассчитать время в секундах, прошедшее с начала суток (30035 в данном случае).
def seconds(hours, minutes, seconds):
    return (hours *3600) + (minutes *60) + (seconds)




# Trivial
# Один человек может поднять вес до 10кг
# TODO: Посчитать количество человек, необходимое для переноски груза
# Примечание: для веса, который может поднять 1 человек, завести отдельную переменную
# Использовтаь операцию приведения типа int()
def peoples_for_work(weight):
    a = 10
    return(int(weight/a))


# Trivial
# На вход поступают два числа в виде строки
# TODO: Необходимо вывести сумму двух чисел
def string_amount(a, b):
    return(int(a)+int(b))




# Easy
# TODO: Поменять местами первую и последнюю цифры четырехзначного числа
def swap(number):
    a = str(number % 10)
    b = str(number // 1000)
    c = str(number % 1000 // 10)
    res = int(a+c+b)
    return res



# Easy
# TODO: Вывести следущее четное число
def next_int(number):
    return((number //2)*2+2)


# Easy
# Пользователь задает целое трехзначное число (например, 478).
# TODO: Необходимо вывести число, полученное из заданного перестановкой цифр в обратном порядке (например, 874).
def revert_number(number):
    a = str(number % 10)
    b = str(number // 100)
    c = str(number % 100 // 10)
    res_numb = int(a + c + b)
    return res_numb
