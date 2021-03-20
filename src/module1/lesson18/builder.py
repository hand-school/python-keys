class House:
    width: int
    length: int
    height: int
    materials: list

    def __init__(self, width=0, length=0, height=0, materials=None):
        self.width = width
        self.length = length
        self.height = height
        self.materials = materials

    def set_width(self, width):
        self.width = width
        return self

    def set_length(self, length):
        self.length = length
        return self

    def set_height(self, height):
        self.height = height
        return self

    def set_materials(self, materials):
        self.materials = materials
        return self


# Пример 0
home0 = House(100, 100, 100, ["M1", "M2"])

# Пример 1
home1 = House().set_width(100).set_height(100).set_materials(["M1", "M2"]).set_length(100)

# Пример 2
home2 = House()
print(home2.__dict__)

width = int(input("Введите ширину "))
home2.set_width(width).set_materials(["M1", "M2"])
print(home2.__dict__)

length = int(input("Введите длину "))
home2.set_length(length)
print(home2.__dict__)

home2.set_height(int(input("Введите высоту ")))
print(home2.__dict__)
