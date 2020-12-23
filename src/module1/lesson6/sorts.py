# Medium
# Реализовать сортировку пузырьком
def bubble_sort(list1):
    list1 = [1, 2, 3, 4, 5, 100]
    for j in range(len(list1)-1):
        for i in range(len(list1) - j - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list[i + 1], list1[i]
    return(list1)


# Medium
# Реализовать сортировку выбором
def selection_sort(list1):
    list = [1, 2, 3, 4, 5, 100]
    for i in range(0, len(list) - 1):
        smallest = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
        list[i], list[smallest] = list[smallest], list[i]
    return(list)


# Medium
# Реализовать сортировку вставками
def insert_sort(list1):
    list1 = [1, 2, 3, 4, 5, 100]
    for i in range(1, len(list1)):
        temp = list1[i]
        j = i - 1
        while (j >= 0 and temp < list1[j]):
            list1[j + 1] = list1[j]
            j = j - 1
        list1[j + 1] = temp
    return (list1)


# Easy
# Найти максимальное и минимальное значение в списке
# Примечание: необходимо использовать встроенную сортировку
def get_max_and_min(list1):
    list = sorted(list1)
    return (list[0], list[-1])


# Hard
# Реализовать быструю сортировку
def quick_sort(list1):
    import random
    if len(list1) <= 1:
        return list1
    else:
        q = random.choice(list1)
    l_nums = [n for n in list1 if n < q]
    e_nums = [q] * list1.count(q)
    b_nums = [n for n in list1 if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)

