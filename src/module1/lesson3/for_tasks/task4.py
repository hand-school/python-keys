# В цилке запрашивать у пользователя числа до тех пор, пока он не введт 0
# Вывести наибольшее число последовательности
a = int(input('Введите число'))
b = []
while a != 0:
    b.append(a)
    a = int(input('Введите число'))
max = b[0]
for i in b:
    if i > max:
        max = i

print(max)
