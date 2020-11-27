class Car:

    # Конструктор класса
    def __init__(self, name, speed, color='RED'):
        self.name = name
        self.speed = speed
        self.color = color

    def __str__(self):
        return 'Car ' + self.name + ' With speed ' + str(self.speed) + ' and color ' + self.color

    def start(self):
        print('Скорость:', self.speed, 'Цвет:', self.color, sep=' ')
        print("Двигатель работает")


bmv = Car('BMW', 250, 'BLACK')
print(bmv.speed)
print(bmv.color)
bmv.start()

msd = Car(name='MSD', speed=249)
print(msd.speed)
print(msd.color)
msd.start()

msd.weight = 1.5
print(msd.weight)

print(bmv)
print(msd)

