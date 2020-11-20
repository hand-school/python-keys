# Training
# TODO: найти длину слова
def use_len(string):
    pass


# Training
# TODO: Функция получает на вход слово и выводит его первый и последний символ через “-”.
# Пример: "Привет" -> "П-т"
def cut_word(string):
    pass


# Training
# TODO: Найти первое вхождения символа symbol в сообщение sms справа и слева
# Результат вывести через запятую
def r_l_find(sms, symbol):
    pass


# Training
# TODO: заменить в строке string символы old_symbol на new_symbol
def replace_chars(string, old_symbol, new_symbol):
    pass


# Training
# TODO: Вернуть количетсов вхождений символа в строку
def count_chars(sms, symbol):
    pass


# Easy
# Используя методы find() и rfind(), напиши функцию,
# которая находит и возвращает индекс второго вхождения символа symbol.
# Если символ встречается один раз,
# программа должна вернуть -1, а если ни одного — вернуть -2.
# ТЕСТЫ НАПИСАТЬ САМОСТОЯТЕЛЬНО
def second_symbol(word, symbol):
    if word.find(symbol) == -1:
        return -2
    elif word.find(symbol) == word.rfind(symbol):
        return -1
    else:
        i = word[word.find(symbol)+1:word.rfind(symbol)+1]
        return i.find(symbol) + word.find(symbol) + 1

        # start = word.find(symbol)
        # end = word.rfind(symbol)
        # return word.find(symbol, [start], [end])
