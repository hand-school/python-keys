# Цикл WHILE
# Пользователь вводит последовательность из любых чисел.
# С помощью цикла while и вложенных условий необходимо написать программу,
# которая просуммирует отдельно все положительные и все отрицательные числа.
# Если пользователь введёт «0», программа должна прекратить работу
# и выдать два результата: сумму положительных чисел и сумму отрицательных чисел,
# отдельно друг от друга в столбик.
summ_positive = 0
summ_negativ = 0
number = (input("Введите последовательность: "))
count = 0
mass = number.split(",")
print(mass)
while count < len(mass):

    if  int(mass[count]) >= 0:
        summ_positive = summ_positive + int(mass[count])

    elif int(mass[count]) < 0:
        summ_negativ = summ_negativ + int(mass[count])

    count += 1

print(summ_positive)
print(summ_negativ)
