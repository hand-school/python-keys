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


home1 = House().set_width(100).set_height(100).set_materials(["M1", "M2"]).set_length(100)
