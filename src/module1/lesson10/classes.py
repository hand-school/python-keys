# Написать класс Машина, имеющий набор атрибутов: скорость, марка, цвет
# Написать МЕТОД get_params(), который в красивом виде представляет на экран параметры машины
# Написать ФУНКЦИЮ compare_speed(car1, car2), которая сравнивает скорости двух машин
# и печатает на экран параметры лучшей машины

class Car:

    def __init__(self, brand, speed, color='RED'):
        self.brand = brand
        self.speed = speed
        self.color = color

    def get_params(self):
        print("Марка: {} \nСкорость:{} \nЦвет:{}".format(self.brand, self.speed, self.color))

    def compare_speed(self, car):
        if car.speed > self.speed:
            car.get_params()
        else:
            self.get_params()

car1 = Car("Audi", 322)

car1.get_params()

car2 = Car("Lada", 1488)

car2.get_params()

car1.compare_speed(car2)
