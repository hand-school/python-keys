# Easy
# На вход передается список из чисел
# Вывести количетсво отрицательных чисел
def find_numbers(list):
    o = 0
    for i in list:
        if i < 0:
            o += 1
    return o


# Easy
# На вход передается список, состоящий из фамилий
# А также буква
# Вывести количетсво фамилий, начинающихся на эту букву
# ИГНОРИРОВТЬ case
def find_people(peoples, filter_char):
    a = 0
    for people in peoples:
        if people[0].lower() == filter_char.lower():
            a += 1
    return a


# Easy
# На вход передается список из чисел
# Заменить в исходном списке все отрицательные числа на 0
# Вернуть полученный список
def change_numbers(list):
    # list2 = []
    # for i in list:
    #     if i >= 0:
    #         list2.append(i)
    #     else:
    #         list2.append(0)
    # return list2

    for i in range(len(list)):
        if list[i] < 0:
            list[i] = 0
    return list
