# 87,80 66,01 1,89 -84,69 -38,19 35,67
string = input()
list1 = string.replace(',', '.').split()


# for i in range(0, len(list1)):
#     list1[i] = float(list1[i])
# print(list1)

# list2 = [float(elem) for elem in list1]
# print(list2)

# ___________MAP___________
# list3 = list(map(float, list1))
# print(list3)

def to_float(string):
    str_flo = float(string)
    return str_flo
#
# list4 = list(map(to_float, list1))
# print(list4)
#
# list5 = []
# for i in range(0, len(list1)):
#     list5.append(to_float(list1[i]))
#
def mapper(func, list1):
    result_list = []
    for i in list1:
        f = func(i)
        result_list.append(f)
    return result_list


list6 = mapper(to_float, list1)
print(list6)

def format_numbers(number):
    return "{:.2f}".format(number)

list7 = list(map(format_numbers, list6))
print(' '.join(list7))


