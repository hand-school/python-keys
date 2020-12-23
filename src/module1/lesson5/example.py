# ____________МНОЖЕСТВА_______________
# s1 = set()
# s2 = {recoursion, 2, 3, 4, 5, 5, 5, 5}
#
# print(s2)
#
# s2.add(6)
# s2.add(7)
# s2.add(8)
# s2.add(5)
# print(s2)
#
# l1 = [recoursion, 2, 3, 4, 5, 6]
#
# if recoursion in l1:
#     print('Число recoursion находится в списке')
#
# if recoursion in s2:
#     print('Число recoursion находится в множестве')

# ____________СЛОВАРИ________________
# d1 = dict()
# d2 = {}
#
# d3 = {
#     'Леша': 20,
#     'Олег': 24,
#     'Озарби': 5,
# }
# print(d3['Леша'])
# print(d3['Олег'])
# print(d3['Озарби'])
#
# d3['Лена'] = 68
#
# print(d3['Лена'])
# print(d3)
#
# if 'Лена' in d3:
#     print(d3['Лена'])
# else:
#     print('Лена не в словаре')


set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {23, 2, 3, 5, 6, 8, 12, 3, 5, 5, 5}

set3 = set()

for elem in set1:
    if elem in set2:
        set3.add(elem)

print(set3)

set4 = set1.intersection(set2)
print(set4)


set5 = set1.difference(set2)
print(set5)

set6 = set2.difference(set1)
print(set6)

set7 = set1.union(set2)
print(set7)