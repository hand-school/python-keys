# ЦИКЛ FOR
# Напиши программу, которая находит в ведённой пользователем
# строке самое короткое слово и печатает его на экран, а также - длину этого слова.
a = input('введите предложение')
b = a.split(' ')  #получили список
len_short = len(b[0])
short_word = b[0]
for i in b:
    if len(i) < len_short:
        len_short = len(i)
        short_word = i

print(short_word, len_short)