# ЦИКЛ FOR
# Пользователь вводит целое положительное число.
# Ему необходимо получить последовательность из трёхзначных чисел,
# сумма цифр которых будет равна введённому им числу.
# Все числа должны быть выведены в столбик.
a = int(input('Введите число'))
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i + j + k == a:
                print(i * 100 + j * 10 + k)
