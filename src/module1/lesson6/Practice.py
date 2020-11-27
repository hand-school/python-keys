# -----------------------------------------------------------
# list1 = [2, 3, 1, 4, 10, -1, -25, 54, 0]
# roll = True
# while roll:
#     roll = False
#     for i in range(len(list1) - 1):
#         if list1[i] > list1[i+1]:
#             list1[i], list1[i+1] = list1[i+1], list1[i]
#
#             roll = True
# print(list1)
# ------------------------------------------------------------

# ------------------------------------------------------------
# _list = [2, 3, 1, 4, 10, -1, -25, 54, 0]
# for i in range(len(_list)):
#     min_index = i
#     for j in range(i + 1, len(_list)):
#         if _list[j] < _list[min_index]:
#             min_index = j
#     _list[i], _list[min_index] = _list[min_index], _list[i]
# print(_list)
# --------------------------------------------------------------
list1 = [2, 5, 7, 100, 3, 1, -3, 201]
list1.sort()
l1 = []
l1.append(list1[0])
l1.append(list1[-1])

print(tuple(l1))
