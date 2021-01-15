# l1 = ["1", "2", "2", "3", "4", "5"]
#
# l2 = list(map(int, l1))
# l3 = list(map(float, l1))
# l4 = list(map(bool, l1))
# print(l2)
# print(l3)
# print(l4)

#
# l5 = [int(i) for i in l1]
# l6 = [float(i) for i in l1]
# l7 = [bool(i) for i in l1]
#
# print(l5)
# print(l6)
# print(l7)
#
# l8 = [i + 5 for i in l5]
# print(l8)
#
# l9 = [int(i) * 2 for i in l1]
# l10 = [str(int(i) * 2) for i in l1]
# print(l9)
# print(l10)

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

# ФУНКЦИИ ГЕНЕРАТОРЫ
# for i in range(0, 10):
#     print(i)


def get_list():
    return [1, 2, 3, 4, 5, 6, 7]


def generate_list(N):
    count = 0
    while count < N:
        count += 1
        yield count


print(generate_list(10))

# for element in generate_list(10):
#     print(element)

generator = generate_list(10)
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())

# _____ЗАДАЧА_______
# ИМЯ ФАМИЛИЯ ОТМЕТКА
# ФАМИЛИЯ (по алфавиту) -> Имя (по алфавиту) -> Отметка (по убыванию)
# Carol Peters 4,Cora Silva 3,Bryan Noto 7,Robert Jackson 10,Veronica Wagner 0,William Rivera 4,Claude Hackworth 8,William Hayes 4,Veronica Wagner 5,Robert Irwin 8

# input_string = 'Carol Peters 4,ALex Peters 5,Cora Silva 3,Bryan Noto 7,Robert Jackson 10,Veronica Wagner 0,William Rivera 4,Claude Hackworth 8,William Hayes 4,Veronica Wagner 5,Robert Irwin 8'
#
# list_of_strings = input_string.split(",")
# print(list_of_strings)
#
# list_of_people = [tuple(string.split(" ")) for string in list_of_strings]
# print(list_of_people)
#
# # Сортировка через sorted
# sorted_list = sorted(list_of_people, key=lambda x: (x[1], x[0], -int(x[2])))
# # Сортировка через метод sort
# list_of_people.sort(key=lambda x: (x[1], x[0], -int(x[2])))
#
# print(sorted_list)
# print(list_of_people)
#
# assert sorted_list == list_of_people

#
# Выводим список, отсортированный по отметкам (по убыванию)
# sorted_list = sorted(no_sorted_list, key=lambda elem: int(elem[2]), reverse=True)
#
# print(sorted_list)
