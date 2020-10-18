# Easy
# На вход подается строка, состоаящая из двух слов, разделенных пробелами
# К примеру: Ivan Ivanov Olegovich
# Вернуть строку формата: "Привет, Ivan Olegovich! Твоя фамилия Ivanov?"
def parse_fio(input_data):
    input_data = input_data.split(' ')
    # return 'Привет, {} {}! Твоя фамилия {}?'.format(input_data[0], input_data[2], input_data[1])
    return 'Привет, {name} {father_name}! Твоя фамилия {last_name}?'.format(
        name=input_data[0],
        father_name=input_data[2],
        last_name=input_data[1]
    )


# Easy
# На вход подается число - индекс знака зодиака
# Вернуть латинское название знака и астрологическое предсказание о жизни и о любви
# Данные взять с сайта https://my.astrofame.com/horoscope/yearly/
# Индексы знаков по порядку с сайта, т.е. Aries - 0 Taurus - 1
# Пример ввода: 0
# Пример вывода: Aries ★★★★ ❤❤❤❤
def horoscope(input_index):
    pass


# Easy
# На вход подается строка, состоящая из цифр, разделенных пробелами
# Дробные числа записаны через запятую
# Необходимо вернуть строчку, в которой будут приведены такие значения, как:
# Сумма всех чисел, среднее арифметическое, максимальное и минимальное значение из списка
# Для форматирование чисел следует использовать "{:.2f}".format(number)).
#
# Пример ввода: 87,80 66,01 1,89 -84,69 -38,19 35,67
# Пример вывода: Sum: 68.49; Mean: 11.41; Min: -84.69; Max: 87.80
def list_params(input_data):
    pass


# Medium
# На вход передается строка, соответствующая формату:
# Marilyn 5,Claire 0,Larry 2,Ward 8,Cynthia 10,William 1
# Т.е. через запятую перечислена информация о разных пользователях,
# которая, в свою очередь, разделена пробелами
# Информация о пользователе: Имя и отметка (от 1 до 10)
# Необходимо определить имя человека с наибольшей отметкой
# Если таких людей несколько - вернуть имя, первое по алфавиту
# Пример ввода: Marilyn 5,Claire 0,Larry 2,Ward 8,Cynthia 10,William 1,Jose 10,Joy 4,Vickey 4,Jonathan 0,Horace 4,James 2,Nora 4,Robert 9,David 6,Jorge 7,Jean 1,Betty 4,Warren 9,Carrie 1,Debra 8,John 0,Maxie 10
# Пример вывода: Cynthia
def max_grade_people(input_data):
    pass
