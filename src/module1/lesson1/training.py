def hello():
    print("hello")
    print("hello")
    print("hello")


def hello_my_friend(name):
    print("Привет, " + name)


def triple_word(string):
    x = 3 * string
    return x


# print(triple_word(input("напиши строку ")))

# a = input("Имя")
# hello_my_frien


# x = 10.5
# print(int(x))

# def swap(number):  # 12345678  -> 82645371
#     a = number % 10  # последнее число = 8
#     b = number // 10000000  # первое число = 1
#     c = (number // 1000) % 100  # 45
#     d = (number // 1000000) % 10  # 2
#     e = (number // 100) % 10  # 6
#     f = (number // 100000) % 10  # 3
#     g = (number // 10) % 10  # 7
#     result1 = b + g * 10 + f * 100 + c * 1000 + e * 100000 + d * 1000000 + a * 10000000
#     print(result1)
#     return result1
#
#
# swap(12345678)

def max(num1, num2, num3):
    if num1 > num2 > num3:
        print(num1)
    elif num2 > num1 > num3:
        print(num2)
    else:
        print(num3)


max(1, 15, 2)
