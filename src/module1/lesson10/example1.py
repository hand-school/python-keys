class Animal:

    def __init__(self, type, weight, color):
        self.type = type
        self.weight = weight
        self.color = color

    def say(self):
        print("Ассалам алейкум, братишка")

    def move(self):
        print('Я - ' + self.type + ' и я двигаюсь!!!')


class Dog(Animal):

    def __init__(self, name, weight, color):
        super().__init__(type='Dog', weight=weight, color=color)
        self.name = name

    def say(self):
        print("Гав гав, братишка")

    def jump(self):
        print('Я {} и я ебать как прыгаю!'.format(self.name))


bob = Dog(name='Bob', weight=12, color='Black')
bob.say()
bob.move()
bob.jump()

print(Dog is Animal)
print(type(bob) is Animal)
print(type(bob) is Dog)
print(isinstance(bob, (Animal, Dog)))

