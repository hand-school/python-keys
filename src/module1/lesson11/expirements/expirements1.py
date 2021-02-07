class Animal:

    def __init__(self, type, weight, color):
        self.type = type
        self.weight = weight
        self.color = color

    def say(self):
        print("Ля какой")

    def run(self):
        print('Убегает ' + self.type)


class Dog(Animal):

    def __init__(self, name, weight, color):
        super().__init__(type='Dog', weight=weight, color=color)
        self.name = name

    def say(self):
        print("Я буду делать кусь")

    def jump(self):
        print('Прыгает за мячом'.format(self.name))


class Cat(Animal):

    def __init__(self, name, weight, color):
        super().__init__(type='Cat', weight=weight, color=color)
        self.name = name

    def say(self):
        print('Я буду тебя царапать')

    def jump(self):
        print('Прыгает на лицо'.format(self.name))

    def run(self):
        print('Бежит ' + self.type)

alex = Dog(name='Alex', weight=12, color='Black')
marge = Cat(name='Marge', weight=5, color='White')
alex.say()
alex.jump()
alex.run()
marge.run()
marge.jump()
marge.say()




