# Easy
# На вход передается список из чисел
# Вывести количетсво отрицательных чисел
# ТЕСТЫ НАПИСАТЬ САМОСТОЯТЕЛЬНО
def find_numbers(list):
    s = 0
    for i in list:
        if i < 0:
            s += 1
    return s


# Easy
# На вход передается список, состоящий из фамилий
# А также буква
# Вывести количетсво фамилий, начинающихся на эту букву
# ИГНОРИРОВТЬ case
def find_people(peoples, filter_char):
    s = 0
    for i in peoples:
        if i[0] == filter_char:
            s += 1
    return s



# Easy
# На вход передается список из чисел
# Заменить в исходном списке все отрицательные числа на 0
# Вернуть полученный список
def change_numbers(list):
    for i in range(len(list)):
        if list[i] < 0:
            list[i] = 0
    return list


# Easy
# Необходио развернуть список
def list_revert(l):
    l.reverse()
    return l


# Easy
# Необходио преобразовать строчку в список символов
# Пример: "Hello" -> ['H', 'e', 'l', 'l', 'o']
def to_char_sequence(string):
    return list(string)


# Easy
# Необходио преобразовать список в строчку
# Пример: ['H', 'e', '123', 'l', '__В'] -> 'He123l__В'
def list_to_string(l):
    string = "".join(l)
    return string


# Medium
# Необходимо вернуть все одинаковые элементы списков
# Примечание:  списки зарание отсортированы по возрастанию
def common_part_of_lists(list1, list2):
    list3 = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list3.append(list1[i])
    return list3


# Medium
# Необходимо вернуть все различные элементы списков
# Примечание:  списки зарание отсортированы по возрастанию
def uncommon_part_of_lists(list1, list2):
    list3 = []
    list4 = []
    i = 0
    j = 0

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list1[i] = 0
                list2[j] = 0

    list3 = list2 + list1

    for i in range(len(list3)):
        if list3[i] != 0:
            list4.append(list3[i])
    #list4.sort()
    return list4

# Training
# Преобразовать исходный список
# ['Ivan Ivanov 5', 'Petr Petrov 3', 'Jeff Downing 10', 'Petr Ivanov 7', 'John Smith 7', 'John Ivanov 6']
# В список с элементами:
# [['Ivan', 'Ivanov', '5'], ['Petr', 'Petrov', '3'], ['Jeff', 'Downing', '10'], ['Petr', 'Ivanov', '7'], ['John', 'Smith', '7'], ['John', 'Ivanov', '6']]
def rebase(list1):
    list2 = []
    list3 = []
    for i in range(len(list1)):
        list2.append(list1[i].split(" "))

    return list2


# Training
# Преобразовать исходный список
# [['Ivan', 'Ivanov', '5'], ['Petr', 'Petrov', '3'], ['Jeff', 'Downing', '10'], ['Petr', 'Ivanov', '7'], ['John', 'Smith', '7'], ['John', 'Ivanov', '6']]
# В список имен
# ['Ivan', 'Petr', 'Jeff', 'Petr', 'John', 'John']
def get_names(list1):
    list2 = []
    list3 = []
    for i in range(len(list1)):
        list2 = list1[i]
        for j in range(len(list2)):
            if j == 0:
                list3.append(list2[j])

    return list3
