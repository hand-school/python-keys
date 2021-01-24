# Создать декоратор, который будет считать время выполнения функции и печатать его на экран
def datetime_logger(f):
    # f - ссылка на функцию, которая декоррируется
    def wrapper(arg1):
        result = f(arg1)
        return result
        from datetime import datetime, timedelta
        return datetime.now() + timedelta(microseconds=arg1)
        print("DATETIME with arg: " + str(arg1))
    return wrapper


@datetime_logger
def amount(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


c = amount(123)
