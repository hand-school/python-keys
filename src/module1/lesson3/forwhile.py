# Training
# TODO: Написать счетчик используя цикл while
def counter(start, step, steps):
    while 0 < steps:
        start = start + step
        steps -= 1

    return start


# Training
# TODO: Найти количество цифр в данном числе используя цикл while
def num_count(number):
    count = 0
    while count < len(str(number)):
       count += 1
    return count


# Training
# TODO: Найти количество символов в строке используя цикл while
def custom_len(number):
    count = 0
    while count < len(str(number)):
        count += 1
    return count


# Training
# TODO: развернуть строчку используя цикл while
def revert(string):
    result = ''
    n = len(string) - 1
    while n >= 0:
        result = result + string[n]
        n -= 1
    return result



# Training
# TODO: Написать счетчик используя цикл for
def counter_for(start, step, steps):
    s = start
    for count in range(steps):
        s = s + step
    return s




# Training
# TODO: Найти количество цифр в данном числе используя цикл for
def num_count_for(number):
    s = 0
    for _ in range(len(str(number))):
        s += 1
    return s


# Training
# TODO: Найти количество символов в строе используя цикл for
def custom_len_for(number):
    s = 0
    for _ in range(len(str(number))):
        s += 1
    return s


# Training
# TODO: развернуть строчку используя цикл for
def revert_for(string):
    result = ''
    n = len(string) - 1
    for n in range(len(string)):
        result = result + string[n]
        n -= 1
    return result


# Easy
# Передается целое положительное число.
# Используя цикл for, напиши программу, которая посчитает квадраты всех чисел
# начиная с 1 и до введённого включительно и выведет на экран их сумму.
def compute(n):
    s = 0
    for count in range(1, n + 1):
        s += count ** 2
        count += 1
    return s
