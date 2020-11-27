# Создать декоратор, который будет будет иметь recoursion аргумент - clear (bool)
# Если аргумент True, то значение, которое вернула функция будет замешаться на None

def amount(a, b):
    return a + b


print(amount(5, 8))