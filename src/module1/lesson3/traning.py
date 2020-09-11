count = 3
a = input('введите логин')
b = input('введите пароль')
right_login = "login"
right_pass = 'pass'
tryy = 1
while (a != right_login or b != right_pass) and tryy < count:
    print('Введите данные снова')
    a = input('введите логин')
    b = input('введите пароль')
    tryy = (tryy + 1)

print("Общая сумма попыток " + str(tryy))
if a == right_login and b == right_pass:
    print('Успешный вход')
else:
    print("ты даун")
