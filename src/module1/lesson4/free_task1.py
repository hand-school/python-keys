# Пользователь вводит строку.
# Используя цикл, напиши программу,
# которая выведет все её символы,
# с их порядковыми номерами.
string = input('Введите строку')
for i in range(0, len(string)):
    print(string[i] + ' - ' + str(i))
