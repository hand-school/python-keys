# Используя методы find() и rfind() напиши программу,
# которая находит символ(полученный от пользователя)
# слева и справа строке(полученный от пользователя)
# и выводит на экран текст, который написан до них, не включая
# сами символы, а текст между ними — пропускает.
# Если символ только один - убрать символы
# от этого символа и до конца.
a = input('Введите строку')
b = input('Введите символ')
left_index = a.find(b)
right_index = a.rfind(b)

if left_index == right_index:
    print(a[:left_index])
else:
    left_slice = a[:left_index]
    right_slice = a[right_index + 1:]
    print(left_slice + ' - ' + right_slice)
