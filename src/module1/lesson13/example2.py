class Color:
    def __init__(self, color):
        self.color = color

    def __add__(self, other):
        return Color(self.color + other.color)


a = 4 + 5
b = "sdf" + "dsf"
print(a)
print(b)

c1 = Color("red")
c2 = Color("white")
c3 = c1 + c2
print(c3.color)

l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 8, 9]
l3 = l1 + l2
print(l3)


def add(a, b):
    return a + b


add(1, 2)
add("dsf", "sdfdsf")
add(c1, c2)
add(l1, l2)
