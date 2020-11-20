# Easy
# На вход передается список из чисел
# Вывести количетсво отрицательных чисел
# ТЕСТЫ НАПИСАТЬ САМОСТОЯТЕЛЬНО
def find_numbers(list):
    s = 0
    for element in list:
        if element < 0:
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
    pass


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


# Training
# Преобразовать исходный список
# ['Ivan Ivanov 5', 'Petr Petrov 3', 'Jeff Downing 10', 'Petr Ivanov 7', 'John Smith 7', 'John Ivanov 6']
# В список с элементами:
# [['Ivan', 'Ivanov', '5'], ['Petr', 'Petrov', '3'], ['Jeff', 'Downing', '10'], ['Petr', 'Ivanov', '7'], ['John', 'Smith', '7'], ['John', 'Ivanov', '6']]
def rebase(list1):
    pass


# Training
# Преобразовать исходный список
# [['Ivan', 'Ivanov', '5'], ['Petr', 'Petrov', '3'], ['Jeff', 'Downing', '10'], ['Petr', 'Ivanov', '7'], ['John', 'Smith', '7'], ['John', 'Ivanov', '6']]
# В список имен
# ['Ivan', 'Petr', 'Jeff', 'Petr', 'John', 'John']
def get_names(list1):
    pass
