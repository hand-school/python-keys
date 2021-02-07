# Сделать вот тут задание)))
# Animal и 2 класса ребенка Cat  и Dog
class Animal:

    def __init__(self, type, speed, eyes, color):
        self.type = type
        self.speed = speed
        self.brand = eyes
        self.color = color

    def say(self):
        print('Вася Ворон')

    def jump(self):
        print('Я шо похож на обезьяну?')


class Cat(Animal):

    def __init__(self, name, speed, eyes, color):
        super().__init__(type='Cat', speed=speed, eyes=eyes, color=color)
        self.name = name

    def say(self):
        print('Meow Meow Meow')

    def jump(self):
        print('Прыжок кошки = 2 метрам'.format(self.name))


class Dog(Animal):

    def __init__(self, name, speed, eyes, color):
        super().__init__(type='Dog', speed=speed, eyes=eyes, color=color)
        self.name = name

    def say(self):
        print('Woof Woof Woof')

    def jump(self):
        print('Собака не хочет прыгать, ей впадлу'.format(self.name))


marge = Cat(name='Marge')
marge.jump()
marge.say()
alex = Dog(name='Alex')
alex.say()
alex.jump()



