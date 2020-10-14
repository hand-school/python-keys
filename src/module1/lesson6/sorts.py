# Medium
# Реализовать сортировку пузырьком
def bubble_sort(list1):
    for j in range(0, len(list1) - 1):
        for i in range(0, len(list1) - 1 - j):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
    return list1



# Medium
# Реализовать сортировку выбором
def selection_sort(list1):
    for i in range(len(list1)):
        min_value = i
        for j in range(i, len(list1)):
            if list1[min_value] > list1[j]:
                min_value = j
        list1[i], list1[min_value] = list1[min_value], list1[i]
    return list1


# Medium
# Реализовать сортировку вставками
def insert_sort(list1):
    for i in range(1, len(list1)):
        key = list1[i]
        j = i - 1
        while j >= 0 and key < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = key
    return list1




# Easy
# Найти максимальное и минимальное значение в списке
# Примечание: необходимо использовать встроенную сортировку
def get_max_and_min(list1):
    list1 = sorted(list1)
    return list1[0], list1[-1]


# Hard
# Реализовать быструю сортировку
def quick_sort(list1):
    pass