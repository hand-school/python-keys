# count = 3
# a = input('введите логин')
# b = input('введите пароль')
# right_login = "login"
# right_pass = 'pass'
# tryy = 1
# while (a != right_login or b != right_pass) and tryy < count:
#     print('Введите данные снова')
#     a = input('введите логин')
#     b = input('введите пароль')
#     tryy = (tryy + 1)
#
# print("Общая сумма попыток " + str(tryy))
# if a == right_login and b == right_pass:
#     print('Успешный вход')
# else:
#     print("ты даун")

#
# count = 0
# while count < 100:
#     count = count + 1
#     print('Кол-во' + str(count))
# print(count)
#
# count = 16
# while 2 < count <= 16:
#     count = count - 1
#     print(count)


number = input('Введите номер через пробел!')
number = number.replace(' ', '')
if len(number) != 11 or number[0] == '0' or number[1] == '0' or number[4] == '0' or not number.isdigit():
    print(0)
else:
    print('+{}({}){}-{}-{}'.format(
        number[0],  # 7
        number[1:4],  # 800
        number[4:7],  # 123
        number[7:9],  # 45
        number[9:11],  # 67
    ))
