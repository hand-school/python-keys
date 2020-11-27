# Создать декоратор, который будет считать время выполнения функции и печатать его на экран

def amount(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


c = amount(123)