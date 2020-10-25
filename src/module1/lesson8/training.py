# 87,80 66,01 1,89 -84,69 -38,19 35,67
# string = input()
# list1 = string.replace(',', '.').split()


# for i in range(0, len(list1)):
#     list1[i] = float(list1[i])
# print(list1)

# list2 = [float(elem) for elem in list1]
# print(list2)

# ___________MAP___________
# list3 = list(map(float, list1))
# print(list3)

# def to_float(string):
#     str_flo = float(string)
#     return str_flo
#
# list4 = list(map(to_float, list1))
# print(list4)
#
# list5 = []
# for i in range(0, len(list1)):
#     list5.append(to_float(list1[i]))
#
# def mapper(func, list1):
#     result_list = []
#     for i in list1:
#         f = func(i)
#         result_list.append(f)
#     return result_list
#
#
# list6 = mapper(to_float, list1)
# print(list6)
#
# def format_numbers(number):
#     return "{:.2f}".format(number)
#
# list7 = list(map(format_numbers, list6))
# print(' '.join(list7))


# birthdays = {'Alise': 'April 1',
#              'Bob': 'Dec 12',
#              'Carol': 'Mar 4'}
# while True:
#     print('Введите имя: ')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + 'is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')


# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '
#             }
#
#
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#
#
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input('Place')
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
# printBoard(theBoard)

# def totalBrought(guests, items):       #функция которая возвращает список продуктов
#     numBrought = 0
#     for k, v in guests.items():         # k - имя гостя(ключ)    v- принесенные продукты
#         numBrought += v.get(item, 0)    # get возвращает item и кол-во. если itam не найдется, то 0
#     return numBrought


