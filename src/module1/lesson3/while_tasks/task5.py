# Цикл WHILE
# Используя счётчик, напиши программу,
# которая выводит в столбик степени двойки с пятой до пятнадцатой включительно.


summ = 0
count = 0
while count <= 15:

    summ = 2**count

    if count >= 5:
        print(summ)


    count = count + 1

