# Easy
# На вход передается список из чисел
# Вывести количетсво отрицательных чисел
# ТЕСТЫ НАПИСАТЬ САМОСТОЯТЕЛЬНО
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


# Easy
# Необходио развернуть список
def list_revert(l):
    # return l[::-1]
    # l2 = []
    # for i in range(len(l)-1, -1, -1):
    #     l2.append(l[i])
    #
    # return l2
    # len_l = len(l)
    # for i in range(0, len_l//2):
    #     x = l[-1 - i]
    #     print(x)
    #     l[-1 - i] = l[i]
    #     l[i] = x
    # return l
    len_l = len(l)
    for i in range(0, len_l // 2):
        l[-1 - i], l[i] = l[i], l[-1 - i]
    return l


# Easy
# Необходио преобразовать строчку в список символов
# Пример: "Hello" -> ['H', 'e', 'l', 'l', 'o']
def to_char_sequence(string):
    l1 = []
    for char in string:
        l1.append(char)
    print(l1)
    return l1


# Easy
# Необходио преобразовать список в строчку
# Пример: ['H', 'e', '123', 'l', '__В'] -> 'He123l__В'
def list_to_string(l):
    a = ''
    for elem in l:
        a += elem
    return a


# Medium
# Необходимо вернуть все одинаковые элементы списков
# Примечание:  списки заиание отсортированы по возрастанию
def common_part_of_lists(list1, list2):
    result = []
    for elem1 in list1:
        for elem2 in list2:
            if elem1 == elem2:
                result.append(elem1)
    return result


# Medium
# Необходимо вернуть все различные элементы списков
# Примечание:  значения в списках отсортированы по возрастанию
def uncommon_part_of_lists(list1, list2):
    result1 = common_part_of_lists(list1, list2)
    result2 = []

    for elem1 in list1:
        if elem1 not in result1:
            result2.append(elem1)

    for elem2 in list2:
        if elem2 not in result1:
            result2.append(elem2)
    return result2


# Training
# Преобразовать исходный список
# ['Ivan Ivanov 5', 'Petr Petrov 3', 'Jeff Downing 10', 'Petr Ivanov 7', 'John Smith 7', 'John Ivanov 6']
# В список с элементами:
# [['Ivan', 'Ivanov', '5'], ['Petr', 'Petrov', '3'], ['Jeff', 'Downing', '10'], ['Petr', 'Ivanov', '7'], ['John', 'Smith', '7'], ['John', 'Ivanov', '6']]
def rebase(list1):
    list2 = [elem.split() for elem in list1]
    return list2



# Training
# Преобразовать исходный список
# [['Ivan', 'Ivanov', '5'], ['Petr', 'Petrov', '3'], ['Jeff', 'Downing', '10'], ['Petr', 'Ivanov', '7'], ['John', 'Smith', '7'], ['John', 'Ivanov', '6']]
# В список имен
# ['Ivan', 'Petr', 'Jeff', 'Petr', 'John', 'John']
def get_names(list1):
    list2 = [elem[0] for elem in list1]
    print([int(elem[2]) for elem in list1])
    return list2
