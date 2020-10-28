# Trivial
# TODO: проверить, явялется ли значение в переменной числом (вернуть true/false)
def is_digit(value):
    return type(value) == type(3)


# Trivial
# TODO: проверить, явялется ли пароль верным
# Пароль: simple123456
def is_password_valid(value):
    a = "simple123456"
    if value == a:
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
    a = 'login123'
    b = 'simple123456'
    if login == a and password == b:
        return 'Успешный вход'
    elif login != a:
        return 'Логин неверный'
    else:
        return 'Неверный пароль'


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
    if a>b:
        return int(1)
    elif a==b:
        return int(0)
    else:
        return int(-1)

# Easy не робит
# Мой возраст. Для заданного 0 < n < 200, рассматриваемого каквозраст человека,
# TODO: Вернуть строку вида: «21 год», «32 года», «12 лет».
def age_description(n):
    if (n >= 2 and n <= 4) or (n % 10 >= 2 and n % 10 <= 4):
        return str(n) + " года"
    elif n == 1:
        return str(n) + " год"
    elif n == 12:
        return str(n) + " лет"
    else:
        return str(n) + " год"



# Easy
# Даны 3 числа
# TODO: Вывести через запятую сначала наибольшее число, затем два оставшихся
# К примеру: return 5, 6, 7
def maximum(a, b, c):
    if a >= b and a >= c:
        return (a, b, c)
    elif b >= a and b >= c:
        return (b, a, c)
    else:
        return (c, a, b)


# Easy не робит
# Треугольник задан длинами своих сторон a, b, c.
# TODO: Проверить, является ли данный треугольник остроугольным(вернуть 0),
# TODO: прямоугольным(вернуть 1) или тупоугольным(вернуть 2).
# Если такой треугольник не существует, вернуть - 1.
def triangle_kind(a, b, c):
    if (a == b and a > c and b > c) or (a == c and a > b and c > b) or (b == c and b > a and c > a):
        return 0
    elif a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a:
        return 1
    elif (a == b and a < c and b < c) or (a == c and a < b and c < b) or (b == c and b < a and c < a):
        return 2
    elif a + b < c or a + c < b or c + b < a:
        return -1


# Easy
# Программа должна умножать или делить два числа.
# При этом, если заданная операция не деление, выполнится умножение.
# Операция деления производится с проверкой:
# при попытке деления на 0 выводится ошибка.
# ТЕСТЫ НАПИСАТЬ САМОСТОЯТЕЛЬНО
def multi_div(a, b, kind):
    pass


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
    pass


# Medium
# Программа получает на вход четыре числа от 1 до 8 каждое.
# Первые два числа — задают координаты первой клетки (номер строки и столбца),
# вторые — координаты второй клетки (гарантируется, что клетки не совпадают).
# Программа должна вернуть True, если выбранные клетки одинакового цвета, иначе — False.
def table_colors(point1_x, point1_y, point2_x, point2_y):
    pass
