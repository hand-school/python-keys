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
    return string.replace(old_symbol, new_symbol)


# Training
# TODO: Вернуть количетсов вхождений символа в строку
def count_chars(sms, symbol):
    return sms.count(symbol)


# Easy
# Используя методы find() и rfind(), напиши функцию,
# которая находит и возвращает индекс второго вхождения символа symbol
# Если символ встречается один раз,
# программа должна вернуть -1, а если ни одного — вернуть -2.
# ТЕСТЫ НАПИСАТЬ САМОСТОЯТЕЛЬНО
def second_symbol(word, symbol):
    counter = word.count(symbol)
    if counter == 1:
        return -1
    if counter == 0:
        return -2
    find1 = word.find(symbol)
    print(find1)
    slice1 = word[find1 + 1:]
    print(slice1)
    find2 = slice1.find(symbol)
    print(find2)
    return find2 + find1 + 1
