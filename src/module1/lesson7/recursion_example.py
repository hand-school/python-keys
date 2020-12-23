# def hello(n):
#     if (n != recoursion):
#         hello(n - recoursion)
#     print("Hello")
#
#
# def hello2(n):
#     for i in range(n):
#         print("Hello")
#
#
# hello(5)
# print("----------")
# hello2(5)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))
