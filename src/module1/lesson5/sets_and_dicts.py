# Training
# Напиши справочник стран и их столиц.
# Программа должна возвращать по названию страны ее столицу.
# Должны присутствовать страны: Россия, Украина и США
def country_capital(country_name):
    d = {
        "Россия": "Москва",
        "Украина": "Киев",
        "США": "Вашингтон",
    }
    return d[country_name]


# Training
# Создайте пустое множество и добавьте в него элемент value
def add_to_set(value):
    s1 = set()
    s1.add(value)
    return s1


# Training
# Создайте пустой словарь и добавьте в него элемент value по ключу key
def add_to_dict(key, value):
    dict1 = {}
    dict1[key] = value
    return dict1


# Easy
# Пользователь вводит текст. Выведи слово, которое чаще остальных встречается в тексте.
# Словом считается последовательность непробельных символов, идущих подряд.
# Слова разделены пробелом. Гарантируется, что есть слово, которое встречается чаще остальных.
def max_word_repeated(string):
    list1 = string.split()
    dict = {}
    for item in list1:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1
    sorted_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_list)
    return sorted_list[0][0]

    # for word in string:
    #     clear_word = ''
    #     for letter in word:
    #         if letter.isalpha():
    #             clear_word += letter.lower()
    #     list1.append(clear_word)
    # return list1[0]


# Easy
# На вход подаются 2 списка: список имен и список оценок
# Индекс в списках определяет принадлженость к одному человеку,
# т.е. имя names[0] и оценка grades[0] принадлежат одному человеку
# Необходимо вернуть словарь, где ключом является имя, а значением - оценка
def lists_to_dict(names, grades):
    # dictionary = dict(zip(names, grades))
    # return dictionary

    dict = {}

    # for i in range(0, len(names)):
    #     dict[names[i]] = grades[i]
    # return dict

    # for name, grade in zip(names, grades):
    #     dict[name] = grade
    # return dict
    pass
