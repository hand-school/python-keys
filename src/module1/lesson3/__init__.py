# def my_range(start, end, i):
#     while start < end:
#         start = start * i
#     yield my_range(start, end, i)
#
#
# for count in my_range(0, 1000, 10):
#     print(count)
# print("the end")
#
#
# list = [24515, 124, -23, 241, -543]
# s = 0
# for i in list:
#     # print(i)
#     if i < 0:
#         s += 1
# print(s)
# peoples = ['Петров', 'Иванов', 'сидоров']
# filter_char = 'с'
# s = 0
# for i in peoples:
#     if i[0] == filter_char:
#         s += 1
# print(s)
word = "152686321984656449"
symbol = "2"

if word.find(symbol) == -1:
    print(-2)
elif word.find(symbol) == word.rfind(symbol):
    print(-1)
else:

    i = word[word.find(symbol)+1:word.rfind(symbol)+1]
    print(i)
    print(word.find(symbol))
    print(i.find(symbol))
    print(i.find(symbol) + word.find(symbol) + 1)