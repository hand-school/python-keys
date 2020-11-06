# =========== WHILE ===============
# a = int(input("Введите цифру: "))
# count = 0
# while count < a:
#     print("Hello")
#     count = count + 1

# a = int(input("Введите цифру: "))
# count = a
# while count > 0:
#     print("Hello")
#     count = count - 1
# =======================================


# login = input("Введите логин: ")
# password = int(input("Введите пинкод: "))
#
# if login == "login" and password == 1234:
#     print("Успешный вход")
# else:
#     print("Пошел нахуй")

# while <условие>:
#     <блок кода>  Выполняется до тех пор, пока верно условие (True)


# =======================================
# login = input("Введите логин: ")
# password = int(input("Введите пинкод: "))
#
# while login != "login" or password != 1234:
#     print("Ты даун?")
#     login = input("Введите логин: ")
#     password = int(input("Введите пинкод: "))
# print("Успешный вход")

# ==============Усовершенствуем=========================
# while input("Введите логин: ") != "login" or int(input("Введите пинкод: ")) != 1234:
#     print("Ты даун?")
# print("Успешный вход")


# =========== СТРОКИ ===============
# string = "Hello"
# print(string[0])
#
# print(len(string))
#
# char_index = 0
# while char_index <= len(string) - 1:
#     print(string[char_index])
#     char_index = char_index + 1

# word = "Hello world"
# print(word[2])  # один символ
# print(word[2:5])  # со 2 по 4 символы
# print(word[3:])  # с 3 символа до конца
# print(word[1:10:2])  # с 1 до 10 с шагом в 2
# print(word[1::2])  # с 1 до конца с шагом в 2
# print(word[10:1:-2])

# word = "Hello world"
# reversed_word = ""  # результат
# char_index = len(word) - 1  # последжний индекс
#
# while char_index >= 0:
#     reversed_word = reversed_word + word[char_index]
#     char_index = char_index - 1
#
# print(word)
# print(reversed_word)
# print(word[::-1])  # не использовать в заданиях (ЧИТ)


# =========== FOR ===============
# for i in <последовательность>:
#     <блок кода>

# range(<start>, <end>, <step>)  Пример: range(1, 5) будет от 1..4  (5 НЕ ВКЛЮЯАЕТСЯ)

# Сравним
# count = 0
# while count < 10:
#     print(count)
#     count = count + 1
#
# for i in range(0, 10):
#     print(i)

# for i in 1, 20, -3, 41, 5, 6:
#     print(i)

# word = "Hello world"
# for i in range(0, len(word)):  # i от 0 до len(word) - 1
#     print(word[i])  # печатаем символ строки word по индексу i

# for char in word:
#     print(char)

# revert на while
# word = "Hello world"
# reversed_word = ""  # результат
#
# char_index = len(word) - 1  # последжний индекс
# while char_index >= 0:
#     reversed_word = reversed_word + word[char_index]
#     char_index = char_index - 1
#
# print(word)
# print(reversed_word)

# revert на for
# word = "Hello world"
# reversed_word = ""
#
# for i in range(len(word) - 1, -1, -1):
#     reversed_word = reversed_word + word[i]
#
# print(word)
# print(reversed_word)
# string = "abgd"
# result = ''
# n = len(string) - 1
# while n >= 0:
#     result = result + string[n]
#     n -= 1
# n = int(input())
# s = 0
# for count in range(1, n + 1):
#     s += count ** 2
#     count += 1
# print(s)
n = int(input())
s = 0
for count in range(1, n + 1, 1/10):
    s += 1
    count += 1
print(s)