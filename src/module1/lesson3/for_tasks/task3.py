# ЦИКЛ FOR
# У компании «Five coding» есть свой способ послания экстренного сигнала,
# если вдруг что-то пошло не так. Вводится список из цифр,
# среди которых есть некоторое количество пятёрок.
# Если их 3 — есть проблема, если 7 — всё в порядке,
# проблема решена, если их нет — всё спокойно.
#
# Помоги компании упростить обработку такого списка.
# Напиши программу, которая подсчитает и выведет на экран
# количество цифр 5 в введённом списке. Если их нет, программа должна вывести -1.

list_of_num = list(map(int, input().split(" ")))
