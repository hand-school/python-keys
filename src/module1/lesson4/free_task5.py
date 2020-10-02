#
#
#

def count(word, symbol):
    counter = 0
    for i in word:
        if symbol == i:
            counter += 1
    return counter


def find(word, symbol):
    for i in range(0, len(word)):
        if symbol == word[i]:
            return i
    return -1


# Индекс N-го вхождения символа в слово
def finder(word, symbol, n):
    counter = 0
    for i in range(0, len(word)):
        if symbol == word[i]:
            counter += 1
            if counter == n:
                return i
    return -1


word = input('Ведите слово ')
sym = input('Введите символ ')
count_sym = count(word, sym)
if count_sym == 0:
    print(-2)
elif count_sym == 1:
    print(-1)
else:
    result = finder(word, sym, 2)
    print(result)


