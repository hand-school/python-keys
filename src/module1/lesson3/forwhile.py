# Training
# TODO: Написать счетчик используя цикл while
def counter(start, step, steps):
    count = 0
    while count < steps:
        count += 1
        start = start + step
    return start


# Training
# TODO: Найти количество цифр в данном числе используя цикл while
def num_count(number):
    # number = str(number)
    # count = 0
    # while count < len(number):
    #     count += 1
    # return count

    count = 0
    while number != 0:
        number = number // 10
        count += 1
    return count


# Training
# TODO: Найти количество символов в строе используя цикл while
def custom_len(number):
    count = 0
    if number == "":
        return 0
    else:
        while number[count] != number[-1]:
            count += 1
    return count + 1


# Training
# TODO: развернуть строчку используя цикл while
def revert(string):
    S = str()
    count = len(string) - 1
    while count <= 0:
        S = S + string[count]
        count -= 1
    return S


# Training
# TODO: Написать счетчик используя цикл for
def counter_for(start, step, steps):
    S = 0
    for count in range(start, start + (step * steps) + step, step):
        S = count
    return S


# Training
# TODO: Найти количество цифр в данном числе используя цикл for
def num_count_for(number):
    number = str(number)
    s = 0
    for _ in number:
        s += 1
    return int(s)


# Training
# TODO: Найти количество символов в строе используя цикл for
def custom_len_for(number):
    number = str(number)
    s = 0
    for _ in number:
        s += 1
    return int(s)


# Training
# TODO: развернуть строчку используя цикл for
def revert_for(string):
    string = str(string)
    S = ""
    for count in range(string[-1], string[0], -1):
        S = S + count
    return S


# Easy
# Передается целое положительное число.
# Используя цикл for, напиши программу, которая посчитает квадраты всех чисел
# начиная с 1 и до введённого включительно и выведет на экран их сумму.
def compute(n):
    pass
