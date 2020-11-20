# Medium
# Реализовать сортировку пузырьком
def bubble_sort(list1):
    for j in range(len(list1) - 1):
        for i in range(len(list1) - j - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
    return list1


# Medium
# Реализовать сортировку выбором
def selection_sort(list1):
    a = len(list1) - 1
    b = 0
    for _ in range(len(list1)):
        elementMax = a
        elementMin = b
        o = False
        q = False
        for i in range(b, a):
            if list1[elementMax] < list1[i]:
                elementMax = i
                o = True
            if list1[elementMin] > list1[i]:
                elementMin = i
                q = True
        if o:
            list1[elementMax], list1[a] = list1[a], list1[elementMax]
        if q:
            list1[elementMin], list1[b] = list1[b], list1[elementMin]
        a = a - 1
        b = b + 1
    return list1


# Medium
# Реализовать сортировку вставками
def insert_sort(list1):
    for i in range(len(list1)):
        Element = list1[i]
        a = i

        while a > 0 and list1[a - 1] > Element:
            list1[a] = list1[a - 1]
            a = a - 1
        list1[a] = Element
    return list1


# Easy
# Найти максимальное и минимальное значение в списке
# Примечание: необходимо использовать встроенную сортировку
def get_max_and_min(list1):
    list = sorted(list1)
    return (list[0], list[-1])


# Hard
# Реализовать быструю сортировку
def quick_sort(list1):
    pass
