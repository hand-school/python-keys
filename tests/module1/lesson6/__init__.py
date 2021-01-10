# def partition(nums, low, high):
#     # Выбираем средний элемент в качестве опорного
#     # Также возможен выбор первого, последнего
#     # или произвольного элементов в качестве опорного
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         # Если элемент с индексом i (слева от опорного) больше, чем
#         # элемент с индексом j (справа от опорного), меняем их местами
#         nums[i], nums[j] = nums[j], nums[i]
#
# def quick_sort(nums):
#     # Создадим вспомогательную функцию, которая вызывается рекурсивно
#     def _quick_sort(items, low, high):
#         if low < high:
#             # This is the index after the pivot, where our lists are split
#             split_index = partition(items, low, high)
#             _quick_sort(items, low, split_index)
#             _quick_sort(items, split_index + 1, high)
#
#     _quick_sort(nums, 0, len(nums) - 1)
#
# # Проверяем, что оно работает
# random_list_of_nums = [22, 5, 1, 18, 99]
# quick_sort(random_list_of_nums)
# print(random_list_of_nums)
list1 = [1, 4, 5, -2, 34, -54, -23, 3, 1, -4]
a = len(list1) - 1
o = False
q = False
b = 0
for _ in range(len(list1)):
    ElementMax = a
    ElementMin = b
    o = False
    q = False
    for i in range(b, a):
        if list1[ElementMax] < list1[i]:
            ElementMax = i
            o = True
        if list1[ElementMin] > list1[i]:
            ElementMin = i
            q = True
    if o:
        list1[ElementMax], list1[a] = list1[a], list1[ElementMax]
    if q:
        list1[ElementMin], list1[b] = list1[b], list1[ElementMin]
    a = a - 1
    b = b + 1
print(list1)