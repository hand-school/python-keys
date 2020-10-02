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
    pass


# Easy
# Необходио преобразовать строчку в список символов
# Пример: "Hello" -> ['H', 'e', 'l', 'l', 'o']
def to_char_sequence(string):
    pass


# Easy
# Необходио преобразовать список в строчку
# Пример: ['H', 'e', '123', 'l', '__В'] -> 'He123l__В'
def list_to_string(l):
    pass


# Medium
# Необходимо вернуть все одинаковые элементы списков
# Примечание:  списки заиание отсортированы по возрастанию
def common_part_of_lists(list1, list2):
    pass


# Medium
# Необходимо вернуть все различные элементы списков
# Примечание:  списки заиание отсортированы по возрастанию
def uncommon_part_of_lists(list1, list2):
    pass
