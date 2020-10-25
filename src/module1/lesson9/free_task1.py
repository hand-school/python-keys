# Создать декоратор, который перед и после выполнения функции будет
# выводить на экран START и STOP, а также печатать на экран значение
# которое возвращает функция
def start_stop(f):
    def wrapper(a, b):
        print('Start')      #код до выполнения функции
        result = f(a, b)    #функция
        print(result)
        print('Stop')        # код после выполнения функции
        return result

    return wrapper


@start_stop                  #обращение к декоратору
def amount(a, b):            # сама функция
    return a + b

a1 = 4
a2 = 8
c = amount(a1, a2)
