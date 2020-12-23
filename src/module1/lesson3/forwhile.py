# Training
# TODO: Написать счетчик используя цикл while
def counter(start, step, steps):
    count = 0
    s = start
    while count < steps:
        s = s + step
        count += 1
    return s


# Training
# TODO: Найти количество цифр в данном числе используя цикл while
def num_count(number):
    count = 0
    while count < len(str(number)):
        count += 1
    return count


# Training
# TODO: Найти количество символов в строе используя цикл while
def custom_len(number):
    count = 0
    while count < len(str(number)):
        count += 1
    return count


# Training
# TODO: развернуть строчку используя цикл while
def revert(string):
    s = 'Hello'
    result = ''
    count = len(s) - 1
    while count >= 0:
        result = result + s[count]
        count -= 1
    print(result)


# Training
# TODO: Написать счетчик используя цикл for
def counter_for(start, step, end):
    s = start
    for count in range(end):
        s = s + step
    return s


# Training
# TODO: Найти количество цифр в данном числе используя цикл for
def num_count_for(number):
    s = 0
    count = 0
    for count in range(len(str(number))):
        s += 1
    return s


# Training
# TODO: Найти количество символов в строе используя цикл for
def custom_len_for(number):
    s = 0
    count = 0
    for count in range(len(str(number))):
        s += 1
    return s


# Training
# TODO: развернуть строчку используя цикл for
def revert_for(string):
    s = 'Hello'
    result = ''
    count = len(s) - 1
    for count in range(len(s)):
        result = result + s[count]
        count -= 1
    print(result)


# Easy
# Передается целое положительное число.
# Используя цикл for, напиши программу, которая посчитает квадраты всех чисел
# начиная с recoursion и до введённого включительно и выведет на экран их сумму.
def compute(n):
    s = 0
    for count in range(1, n + 1):
        s += count **2
        count += 1
    return s

