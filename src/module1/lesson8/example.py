# lambda x: x
#
# def foo(string):
#     return int(string) * 2 + 10
#
#
# list_of_str = ['1', '2', '3', '4']

# result1 = [foo(x) for x in list_of_str]

# result2 = [int(x) * 2 + 10 for x in list_of_str]

# result3 = list(map(foo, list_of_str))

# result4 = list(map(lambda x: int(x) * 2 + 10, list_of_str))
#
# print(result1, result2, result3, result4, sep='\n')

# func = lambda x: int(x) * 2 + 10   #  ТАК ДЕЛАТЬ НЕ НАДО
#
# def func(x):
#     return int(x) * 2 + 10
#
# print(func(2))

# lambda a, b: a + b

# _____ЗАДАЧА_______
# ИМЯ ФАМИЛИЯ ОТМЕТКА
# ФАМИЛИЯ (по алфавиту) -> Имя (по алфавиту) -> Отметка (по убыванию)
# Carol Peters 4,Cora Silva 3,Bryan Noto 7,Robert Jackson 10,Veronica Wagner 0,William Rivera 4,Claude Hackworth 8,William Hayes 4,Veronica Wagner 5,Robert Irwin 8
# input_string = 'Carol Peters 4,Cora Silva 3,Bryan Noto 7,Robert Jackson 10,Veronica Wagner 0,William Rivera 4,Claude Hackworth 8,William Hayes 4,Veronica Wagner 5,Robert Irwin 8'
#
# input_list = input_string.split(',')
#
# no_sorted_list = [tuple(x.split(' ')) for x in input_list]

# sorted_list = sorted(no_sorted_list, key=lambda x: (x[1], x[0], -int(x[2])))
#
# print(sorted_list)

# Выводим список, отсортированный по отметкам (по убыванию)
# sorted_list = sorted(no_sorted_list, key=lambda elem: int(elem[2]), reverse=True)
#
# print(sorted_list)
