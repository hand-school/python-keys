# Создать декоратор, который перед и после выполнения функции будет
# выводить на экран START и STOP, а также печатать на экран значение
# которое возвращает функция

def logger(f):
    # f - ссылка на функцию, которая декоррируется
    def wrapper(arg1, arg2):
        print("START")
        result = f(arg1, arg2)
        print(result)
        print("STOP")
        return result

    return wrapper


@logger
def amount(a, b):
    return a + b


с = amount(5, 8)
