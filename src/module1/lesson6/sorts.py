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
    pass


# Medium
# Реализовать сортировку вставками
def insert_sort(list1):
    pass


# Easy
# Найти максимальное и минимальное значение в списке
# Примечание: необходимо использовать встроенную сортировку
def get_max_and_min(list1):
    pass


# Hard
# Реализовать быструю сортировку
def quick_sort(list1):
    pass
