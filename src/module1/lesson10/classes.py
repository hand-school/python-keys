# Написать класс Машина, имеющий набор атрибутов: скорость, марка, цвет
# Написать МЕТОД get_params(), который в красивом виде представляет на экран параметры машины
# Написать ФУНКЦИЮ compare_speed(car1, car2), которая сравнивает скорости двух машин
# и печатает на экран параметры лучшей машины

class Car:
    def __init__(self, speed, brand, color):
        self.speed = speed
        self.brand = brand
        self.color = color

    def get_params(self):
        print("speed = {}, brand = {}, color = {}".format(self.speed, self.brand, self.color))

    def compare_speed(self, car):
        if car.speed > self.speed:
            car.get_params()
        else:
            self.get_params()


car1 = Car(120, "Mercedes", "white")
car1.get_params()
car2 = Car(130, "BMW", "Black")
car2.get_params()
car1.compare_speed(car2)
