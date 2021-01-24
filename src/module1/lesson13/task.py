# Создать 3х наследников класса Maximum, реализующих метод max разными способами
class Maximum:
    def max(self, a, b):
        pass


class Maximum1(Maximum):
    def max(self, a, b):
        if a > b:
            print(a)
        elif a == b:
            print(a, b)
        else:
            print(b)


class Maximum2(Maximum):
    def max(self, a, b):
        print(max(a, b))


class Maximum3(Maximum):
    def max(self, a, b):
        maxim = a
        if maxim < b:
            maxim = b
        else:
            maxim = a
        print(maxim)


m1 = Maximum1()
m1.max(15, 12)

m2 = Maximum2()
m2.max(111113, 1212)

m3 = Maximum3()
m3.max(121, 11)


# Реализовать функцию нахождения максимума не зависящую от конкретного класса наследника Maximum
def get_maximum(a, b, maxim):
    maxim = a
    if maxim < b:
        maxim = b
    else:
        maxim = a
    return maxim

