# Создать декоратор, который будет считать время выполнения функции и печатать его на экран
import datetime
def counter(f):
    def wrapper(n):
        start_time = datetime.datetime.now()
        result = f(n)
        end_time = datetime.datetime.now()
        diff_time = end_time - start_time
        print(diff_time)
        return result

    return wrapper

@counter
def amount(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


c = amount(12376)
print(c)