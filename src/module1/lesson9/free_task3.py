# Создать декоратор, который будет будет иметь 1 аргумент - clear (bool)
# Если аргумент True, то значение, которое вернула функция будет замешаться на None
def logger(clear=False):
    def decor(f):
        # f - ссылка на функцию, которая декоррируется
        def wrapper(arg1, arg2):
            if clear:
                return None
            else:
                return f(arg1, arg2)

        return wrapper

    return decor


@logger
def amount(a, b):

    return a + b


print(amount(5, 8))


# @logger(fuck=True)
# def get_current_date_plus_days(days):
#     from datetime import datetime, timedelta
#     return datetime.now() + timedelta(days=days)
#
#
# c = get_current_date_plus_days(2)
# print(c)

#

