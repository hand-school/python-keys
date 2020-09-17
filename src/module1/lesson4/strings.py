# Training
# TODO: найти длину слова
def use_len(string):
    return len(string)


# Training
# TODO: Функция получает на вход слово и выводит его первый и последний символ через “-”.
# Пример: "Привет" -> "П-т"
def cut_word(string):
    return string[0] + '-' + string[len(string) - 1]


# Training
# TODO: Найти первое вхождения символа symbol в сообщение sms справа и слева
# Результат вывести через запятую
def r_l_find(sms, symbol):
    a = sms.find(symbol)
    b = sms.rfind(symbol)
    return a, b


# Training
# TODO: заменить в строке string символы old_symbol на new_symbol
def replace_chars(string, old_symbol, new_symbol):
    pass


# Training
# TODO:
def count_chars(sms, symbol):
    return sms.count(symbol)


# Easy
# Используя методы find() и rfind(), напиши функцию,
# которая находит индекс второго вхождения символа symbol
# в неё и выводит его на экран. Если символ встречается один раз,
# программа должна вернуть -1, а если ни одного — вернуть -2.
# ТЕСТЫ НАПИСАТЬ САМОСТОЯТЕЛЬНО
def second_symbol(word, symbol):
    pass
