# Training
# TODO: Написать счетчик используя цикл while
def counter(start, step, steps):
    a = steps
    b = start
    while a > 0:
        a = a - 1
        b = b + step
    return b


# Training
# TODO: Найти количество цифр в данном числе используя цикл while
def num_count(number):
    a = 1
    while number // 10 > 0:
        a += 1
        number //= 10
    return a


# Training
# TODO: Найти количество символов в строе используя цикл while
def custom_len(number):
    a = len(number) - 1
    c = 0
    while a > -1:
        c += 1
        a -= 1
    return c


# Training
# TODO: развернуть строчку используя цикл while
def revert(string):
    rev = ''
    c = len(string) - 1
    while c > -1:
        rev += string[c]
        c -= 1
    return rev


# Training
# TODO: Написать счетчик используя цикл for
def counter_for(start, step, end):
    a = start
    for i in range(0, end):
        a = a + step
    return a


# Training
# TODO: Найти количество цифр в данном числе используя цикл for
def num_count_for(number):
    a = len(str(number))
    b = 0
    for i in range(0, a):
        b += 1
    return b


# Training
# TODO: Найти количество символов в строе используя цикл for
def custom_len_for(number):
    a = 0
    for i in range(len(number)):
        a += 1
    return a


# Training
# TODO: развернуть строчку используя цикл for
def revert_for(string):
    a = ''
    for i in range(len(string) - 1, -1, -1):
        a += string[i]
    return a


# Easy
# Передается целое положительное число.
# Используя цикл for, напиши программу, которая посчитает квадраты всех чисел
# начиная с 1 и до введённого включительно и выведет на экран их сумму.
def compute(n):
    a = 0
    for i in range(1, n + 1):
        a += i ** 2
    return a
