import random

default_brands = ['BMV', 'Mercedes', 'Audi']
default_colors = ['White', 'Red', 'Black']


class Bike:

    def __init__(
            self,  # ссылка на себя
            speed,  # скорость автомобиля
            brand,  # бренд автомобиля
            color  # цвет автомобиля
    ):
        self.speed = speed
        self.brand = brand
        self.color = color


class Car:

    @staticmethod
    def create():
        return Car(random.randint(100, 350), random.choice(default_brands), random.choice(default_colors))

    def copy(self):
        return Car(self.speed, self.brand, self.color)

    def __init__(
            self,  # ссылка на себя
            speed,  # скорость автомобиля
            brand,  # бренд автомобиля
            color  # цвет автомобиля
    ):
        self.id = random.randint(1, 10000000)
        self.speed = speed
        self.brand = brand
        self.color = color

    # Преобрзаование объекта в строку
    def __str__(self) -> str:
        return '''
        Car {self_id} with:
            speed: {speed}
            brand: {brand}
            color: {color}
        '''.format(self_id=self.id, speed=self.speed, brand=self.brand, color=self.color)

    # Сравнение объектов
    def __eq__(self, o):
        if o is None:
            return False
        if self is o:
            return True
        if not isinstance(o, Car):
            return False
        if self.speed != o.speed or self.brand != o.brand or self.color != o.color:
            return False
        return True


car1 = Car.create()
car2 = Car.create()
bike = Bike(12, "Loh", "Shit")

print(car1)
print(car2)

print(car1.__eq__(car2))
print(car1.__eq__(car1))
print(car1 == car1)
print(car1 is car1)
print(car1 is car2)
print(car2.__eq__(car1))
print(car1.__eq__(bike))
print(car1.__eq__(None))
print(car1.__eq__("sdfdsfdsf"))

car1_copy = car1.copy()

print("-----------------")
print(car1 is car1_copy)
print(car1 == car1_copy)

print("-----------------")
car1_link_copy = car1
print(car1 is car1_link_copy)
print(car1 == car1_link_copy)

print(car1.speed)
car1_link_copy.speed = 450
print(car1.speed)


