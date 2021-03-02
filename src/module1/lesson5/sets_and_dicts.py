# Training
# Напиши справочник стран и их столиц.
# Программа должна возвращать по названию страны ее столицу.
# Должны присутствовать страны: Россия, Украина и США
def country_capital(country_name):
    _mass = {
        "Россия": "Москва",
        "Украина": "Киев",
        "США": "Вашингтон"
    }
    return _mass[country_name]


# Training
# Создайте пустое множество и добавьте в него элемент value
def add_to_set(value):
    _mass = set()
    _mass.add(value)
    return _mass


# Training
# Создайте пустой словарь и добавьте в него элемент value по ключу key
def add_to_dict(key, value):
    _dict = {}
    _dict[key] = value
    return _dict


# Easy
# Пользователь вводит текст. Выведи слово, которое чаще остальных встречается в тексте.
# Словом считается последовательность непробельных символов, идущих подряд.
# Слова разделены пробелом. Гарантируется, что есть слово, которое встречается чаще остальных.
def max_word_repeated(string):
    iMax = 0
    strRes = 'ы'

    for i in string.split():
        if string.split().count(i) >= iMax:
            iMax = string.split().count(i)
    for i in string.split():
        if string.split().count(i) == iMax:
            if strRes > i:
                strRes = i
    return strRes


# Easy
# На вход подаются 2 списка: список имен и список оценок
# Индекс в списках определяет принадлженость к одному человеку,
# т.е. имя names[0] и оценка grades[0] принадлежат одному человеку
# Необходимо вернуть словарь, где ключом является имя, а значением - оценка
def lists_to_dict(names, grades):

    _dict = {}
    for i in range(len(names)):
        for j in range(len(grades)):
            _dict[names[j]] = grades[j]

    return (_dict)
