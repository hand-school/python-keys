import sqlite3


class SQLiter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_user_sex(self, user_id):
        """Получаем пола пользователя"""
        with self.connection:
            result = self.cursor.execute("SELECT sex FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return str(result)

    def get_user_target(self, user_id):
        """Получаем цели пользователя"""
        with self.connection:
            result = self.cursor.execute("SELECT target FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return str(result)

    def user_exists(self, user_id):
        """Проверяем, есть ли уже пользлватель в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, status=True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `status`) VALUES(?,?)", (user_id, status))

    def add_sex(self, user_id, sex):
        """Добавление данных о поле полльзователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `sex` = ? WHERE user_id = ? ", (sex, user_id))

    def add_target(self, user_id, target):
        """Добавление данных о цели пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `target` = ? WHERE user_id = ?",
                                       (target, user_id))

    def delete_user(self, user_id, status):
        """Удаления пользователя из БД"""
        with self.connection:
            return self.cursor.execute("delete from `users`  WHERE `user_id` = ? and 'status' = ?", (user_id, status))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
