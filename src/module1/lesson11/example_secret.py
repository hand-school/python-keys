class User:
    def __init__(self, email, login, password, name, phone):
        self.email = email
        self.login = login
        self.password = password
        self.name = name
        self.phone = phone
        self.is_login = False

    def log_in(self, login, password):
        if login == self.login and password == self.password:
            self.is_login = True
            print("Авторизация прошла успешно")
        else:
            print("Неверный логин или пароль")

    def log_out(self):
        self.__check_log_in()
        self.is_login = False
        print("Вы успешно вышли из учетной записи")

    def send_email(self, email, msg):
        self.__check_log_in()
        print('''
        Письмо.
           Отправитель: {self_email} 
           Получатель: {other_email} 
           Сообщение: {message} 
        '''.format(self_email=self.email, other_email=email, message=msg))

    def __check_log_in(self):
        assert self.is_login, "Вы не авторизованы!"

    def get_phone(self):
        return self.phone


user = User("test@mail.ru", "test", "simple123456", "Nikita", "+7 (900) 900 90-90")

# МОЖЕМ ИЗМЕНИТЬ ПАРОЛЬ
# user.password = "1"
# user.log_in("test", "1")
# user.send_email("test2@mail.ru", "Привет, Я - Никита!")

# МОЖЕМ ПОЛУЧИТЬ НЕЛЕГАЛЬНЫЙ ДОСТУП
# user.log_in(user.login, user.password)
# user.send_email("test2@mail.ru", "Привет, Я - Никита!")

# МОЖЕМ ПРОСТО ВСЕ ДЕЛАТЬ
# user.is_login = True
# user.send_email("test2@mail.ru", "Привет, Я - Никита!")

# user.log_in("test", "simple123456")
# user.send_email("test2@mail.ru", "Привет, Я - Никита!")
