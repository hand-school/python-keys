# Пользователь вводит текст через пробел
# Вывести длину наименьшего слова
# Дополнение: вывести длину наибольшего слова
# А также и сами эти слова
a = input('Введите тест')
list1 = a.split()
a_max = len(list1[0])
a_min = len(list1[0])
b_min = ''
b_max = ''
for i in list1:
    if len(i) < a_min:
        a_min = len(i)
        b_min = i
    elif len(i) > a_max:
        a_max = len(i)
        b_max = i
print(b_min, a_min, b_max, a_max)

