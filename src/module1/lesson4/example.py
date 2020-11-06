# ______________СТРОКИ___________________
# str0 = ""
# str1 = str()
# print(str1)

# string = "Hello world"
# print(string[4])
# print(string[1:8])
# print(string[::2])
# print(string[::-1])

# o_index = string.find("o")
# print("o_index = " + str(o_index))
#
# or_index = string.find("or")
# print("or_index = " + str(or_index))
#
# o_right_index = string.rfind("o")
# print("o_right_index = " + str(o_right_index))
#
# length = len(string)
# print("length = " + str(length))
#
# o_count = string.count("o")
# print("o_count = " + str(o_count))
#
# or_count = string.count("or")
# print("or_count = " + str(or_count))
#
# o_replace = string.replace("o", "OOOOO")
# print(o_replace)
#
# lower_str = "HELLO WORLD".lower()
# print(lower_str)
#
# upper_str = "hello world".upper()
# print(upper_str)
#
# print("A".isupper())
# print("A".isalpha())
# print("A".isdecimal())
# print("10".isdigit())
# print("11".isnumeric())

# string = "   hello   " * 10
# print(string)
# print(string.strip())


# ______________СПИСКИ___________________
# l1 = [1, 2, 3, 4, 5, 6]
# print(l1)

# l2 = ['1asd', 'asda', '23423']
# print(l2)
#
# l3 = [1, 2, 3.3, 'sdfdsf', True]
# print(l3)
#
# l4 = []
# l5 = list()
# print(l4)
# print(l5)

# print(l1[3])
# print(l1[1:6])
# print(l1[0:6:2])

# print(len(l1))

# list_to_str_1 = "".join(l2)
# print(list_to_str_1)

# list_to_str_2 = "   ".join(l2)
# print(list_to_str_2)

# list_of_str1 = list(map(str, l1))
# # РАВНОСИЛЬНО
# list_of_str2 = []
# for i in l1:
#     list_of_str2.append(str(i))
#
# print(l1)
# print(list_of_str1)
# print(list_of_str2)

# list_to_str_3 = "---".join(list(map(str, l1)))
# print(list_to_str_3)

# string_to_list = ("hello " * 10).strip()
# print(string_to_list)
# new_list = string_to_list.split(" ")
# print(new_list)
#
# string_to_list_2 = "hello_hello_hello_hello_hello hello hello hello hello hello"
# new_list_2 = string_to_list_2.split("_")
# print(new_list_2)
list1 = [1, 2, 3, 4, 5, 11, 123, 324, 456]
list2 = [-11, -5, 0, 1, 2, 3, 4, 5, 331, 456, 1024, 23]
list3 = []
list4 = []
i = 0
j = 0
# for i in range(len(list2)):
#     for j in range(len(list1)):
#         if list2[i] != list1[j]:
#             list3.append(list2[i])
#         # elif list1[j] != list2[i]:
#         #     list3.append(list2[i])
list3 = list1 + list2
list4 = list(set(list3))
# for i in list3:
#   if i not in list4:
#     list4.append(i)
# # for i in range(len(list3)):
# #     if list3[i] != 0:
# #         list4.append(list3[i])
# #
print(list4)






