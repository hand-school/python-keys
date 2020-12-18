class Animal:
    def say(self):
        pass


class Cat(Animal):
    def say(self):
        print("Мяу")


class Dog(Animal):
    def say(self):
        print("Гав")


class Parrot(Animal):
    def say(self):
        print("Чик чирик")


l = [Cat(), Dog(), Parrot(), Cat(), Cat()]

for animal in l:
    animal.say()

Cat().say()
Dog().say()
