# Пользователь вводит число больше 1 (Пусть N)
# После этого вводит N чисел, которые необходимо записать в список
# Вывести наибольшее и наименьшие числа списка
#
a = int(input('число'))
li1 = []

counter = 0
while counter < a:
    b = int(input('еще число'))
    li1.append(b)
    counter += 1

print(li1)

dig_min = li1[0]
dig_max = li1[0]
for i in li1:
    if dig_min < i:
        dig_min = i
    elif dig_max > i:
        dig_max = i

print(dig_max, dig_min)