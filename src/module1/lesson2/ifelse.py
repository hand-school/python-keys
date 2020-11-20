# Trivial
# TODO: проверить, явялется ли значение в переменной числом (вернуть true/false)
def is_digit(value):
    return type(value) == type(3)


# Trivial
# TODO: проверить, явялется ли пароль верным
# Пароль: simple123456
def is_password_valid(value):
    correct_password = 'simple123456'
    return value == correct_password


# Trivial
# TODO: проверить, есть ли у пользователя доступ
# Пароль: simple123456 Логин: login123
# Примечание: сначала произвести проверку логина, а затем пароля
# если введен неверный логин - вывести "Логин неверный"
# если введен верный логин, но неверный пароль - вывести "Неверный пароль"
# если все введено вверно - вывести "Успешный вход"
def sign_in(login, password):
    correct_log = 'login123'
    correct_pass = 'simple123456'
    if login == correct_log:
        if password == correct_pass:
            return "Успешный вход"
        else:
            return "Неверный пароль"
    else:
        return "Логин неверный"


# Trivial
# TODO: вернуть 1, если строка
# TODO: вернуть 2, если целое число
# TODO: вернуть 3, если дробное число
# TODO: вернуть 4, если bool
def check_type(value):
    if type(value) == str:
        return 1
    elif type(value) == int:
        return 2
    elif type(value) == float:
        return 3
    else:
        return 4

    # Trivial


# На вход подаются два числа.
# TODO: Вывести результат сравнения
# Если первое больше второго, вывести 1,
# Если равны - 0,
# Если второе больше первого - -1
def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


# Easy
# Мой возраст. Для заданного 0 < n < 200, рассматриваемого каквозраст человека,
# TODO: Вернуть строку вида: «21 год», «32 года», «12 лет».
def age_description(n):
    if n % 100 == 11 or n % 100 == 12 or n % 100 == 13 or (n % 10 != 1 and n % 10 != 2 and n % 10 != 3):
        n = str(n)
        return n + ' лет'
    elif n % 10 == 1:
        n = str(n)
        return n + ' год'
    else:
        n = str(n)
        return n + ' года'


# Easy
# Даны 3 числа
# TODO: Вывести через запятую сначала наибольшее число, затем два оставшихся
# К примеру: return 5, 6, 7
def maximum(a, b, c):
    if a > b and a > c:
        return a, b, c
    elif c > b:
        return c, b, a
    else:
        return b, c, a


# Easy
# Треугольник задан длинами своих сторон a, b, c.
# TODO: Проверить, является ли данный треугольник остроугольным(вернуть 0),
# TODO: прямоугольным(вернуть 1) или тупоугольным(вернуть 2).
# Если такой треугольник не существует, вернуть - 1.
def triangle_kind(a, b, c):
    pass
    if c > a+b or b > c+a or a > c+b:
        return -1
    elif c**2 + b**2 == a**2 or c**2 + a**2 == b**2 or a**2 + b**2 == c**2:
        return 1
    elif c**2 + b**2 < a**2 or c**2 + a**2 < b**2 or a**2 + b**2 < c**2:
        return 2
    else:
        return 0



# Easy
# Программа должна умножать или делить два числа.
# При этом, если заданная операция не деление, выполнится умножение.
# Операция деления производится с проверкой:
# при попытке деления на 0 выводится ошибка.
# ТЕСТЫ НАПИСАТЬ САМОСТОЯТЕЛЬНО
def multi_div(a, b, kind):
    if kind == "div":
        if b == 0:
            return 'error'
        else:
            return a/b
    else:
        return a*b


# Medium
# Программа получает на вход четыре числа от 1 до 8 каждое.
# Первые два числа — задают координаты местонахождения ладьи в данный момент
# (номер строки и столбца),
# два других числа — координаты клетки, в которую необходимо переместить фигуру
# (гарантируется, что клетки не совпадают).
# Программа должна вернуть True",
# если из первой клетки ходом ладьи можно попасть во вторую,
# иначе — False.
def can_move(start_x, start_y, end_x, end_y):
    if start_x == end_x or start_y == end_y:
        return True
    else:
        return False


# Medium
# Программа получает на вход четыре числа от 1 до 8 каждое.
# Первые два числа — задают координаты первой клетки (номер строки и столбца),
# вторые — координаты второй клетки (гарантируется, что клетки не совпадают).
# Программа должна вернуть True, если выбранные клетки одинакового цвета, иначе — False.
def table_colors(point1_x, point1_y, point2_x, point2_y):
    pass
