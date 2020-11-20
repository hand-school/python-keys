# list1 = [0, 1, 2, 3, 4, 45, 32, 234, 5, 6, 7]
#
# sorted_list = sorted(list1)
# print(sorted_list)
#
# reversed_sorted_list = sorted(list1, reverse=True)
# print(reversed_sorted_list)
#
# list1.sort()
# print(list1)
#
# list1.sort(reverse=True)
# print(list1)

def sort_with_opt(list1):
    is_changed = False
    check_iter = 0
    for j in range(len(list1) - 1):
        for i in range(len(list1) - j - 1):
            if list1[i] > list1[i + 1]:
                is_changed = True
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
        check_iter += 1
        if not is_changed:
            break
        else:
            is_changed = False
    print(check_iter)
    return list1


def sort_without_opt(list1):
    check_iter = 0
    for j in range(len(list1) - 1):
        for i in range(len(list1) - j - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
        check_iter += 1

    print(check_iter)
    return list1


list1 = [0, 1, 2, 3, 4, 45, 32, 234, 5, 6, 7]
sort_with_opt(list1)
sort_without_opt(list1)
