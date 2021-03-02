# Пользователь вводит строку.
# Используя цикл, напиши программу,
# которая выведет все её символы,
# с их порядковыми номерами.
string = input()
count = 0

for count in range(len(string)):
    print("Элемент №{}".format(count), string[count])
    count += 1
