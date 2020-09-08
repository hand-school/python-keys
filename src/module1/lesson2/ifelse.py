# Trivial
# TODO: проверить, явялется ли значение в переменной числом (вернуть true/false)
def is_digit(value):
    if type(value) == int:
        return True
    else:
        return False


# Trivial
# TODO: проверить, явялется ли пароль верным
# Пароль: simple123456
def is_password_valid(value):
    if value == "simple123456":
        return True
    else:
        return False


# Trivial
# TODO: проверить, есть ли у пользователя доступ
# Пароль: simple123456 Логин: login123
# Примечание: сначала произвести проверку логина, а затем пароля
# если введен неверный логин - вывести "Логин неверный"
# если введен верный логин, но неверный пароль - вывести "Неверный пароль"
# если все введено вверно - вывести "Успешный вход"
def sign_in(login, password):
    c = "Логин неверный"
    d = "Неверный пароль"
    e = "Успешный вход"
    if login != 'login123':
        return c
    elif login == 'login123' and password != "simple123456":
        return d
    else:
        return e


# Trivial
# TODO: вернуть 1, если строка
# TODO: вернуть 2, если целое число
# TODO: вернуть 3, если дробное число
# TODO: вернуть 4, если bool
def check_type(value):
    if type(value) == str:
        return 1
    if type(value) == int:
        return 2
    if type(value) == float:
        return 3
    if type(value) == bool:
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
    if a == b:
        return 0
    if a < b:
        return -1


# Easy
# Мой возраст. Для заданного 0 < n < 200, рассматриваемого каквозраст человека,
# TODO: Вернуть строку вида: «21 год», «32 года», «12 лет».
def age_description(n):
    pass

# Easy
# Треугольник задан длинами своих сторон a, b, c.
# TODO: Проверить, является ли данный треугольник остроугольным(вернуть 0),
# TODO: прямоугольным(вернуть 1) или тупоугольным(вернуть 2).
# Если такой треугольник не существует, вернуть - 1.
def triangle_kind(a, b, c):
    if c ** 2 > (a ** 2) + (b ** 2):
        return 1
    elif c ** 2 < (a ** 2) + (b ** 2):
        return 0
    elif ((a ** 2) + (b ** 2)) ** 0.5 == c:
        return 2
    elif a > b + c or b > a + c or c > a + b:
        return -1
