# Пользователь вводит число больше 1 (Пусть N)
# После этого вводит N чисел, которые необходимо записать в список
# Вывести наибольшее и наименьшие числа списка
#

n = int(input("введите размер массива: "))
_list = []
i = 0

if n > 1:
    _max = _list[0]
    _min = _list[0]

    for i in range(n):
        _list.append(int(input()))
        i += 1
    print(_list)

    for index_max in _list:

        if index_max > _max:
            _max = index_max
    print("Наибольший элемент: ", _max)

    for index_min in _list:

        if index_min < _min:
            _min = index_min
    print("Наименьший элемент: ", _min)
else:
    print("Неверное значение")
