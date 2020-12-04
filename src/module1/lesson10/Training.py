#Создать класс робот 3 экземпляра класса(1 из них именнованый), 5 полей, 3 метода, 1 из полей по умолчанию

class Robot:

    def __init__(self, name, signal_type, strength, step = 0, distance = 0, battery = 100):
        self.name = name
        self.step = step
        self.signal_type = signal_type
        self.battery = battery
        self.distance = distance
        self.strength = strength

    def motion(self):
        if self.step < self.battery:
            if self.step == 0:
                print("Робот {} не двинулся\n".format(self.name))
            elif self.step < 0:
                print("Робот {} сделал {} шагов назад\n".format(self.name, self.step))
                self.battery -= self.step
                self.distance += self.step
            else:
                print("Робот {} сделал {} шагов и остановился\n".format(self.name, self.step))
                self.battery -= self.step
                self.distance += self.step

    def warcry(self):
        print("Победил {}".format(self.name))
        print(self.signal_type)

    def fight(self, robot):
        if robot.distance == self.distance:
            if robot.strength > self.strength:
                robot.warcry()
                self.battery = 0

    def recharge(self):

        if 0<self.battery <= 20:
            print("Осталось {}% заряда. Скоро робот {} потеряет возможность двигаться!\n".format(self.battery, self.name))
        elif self.battery == 0:
            print("Заряд робота {} иссяк!\n".format(self.name))
        else:
            print("У робота {} осталось {}% заряда\n".format(self.name, self.battery))


robot1 = Robot(name="T1000", signal_type="Doomsday is here!", strength=10)
robot1.step = int(input("Сколько шагов пройдет робот?".format(robot1.name)))
robot1.motion()
robot1.recharge()

robot2 = Robot(name="T800", signal_type="For John Conor!", strength=12)
robot2.step = int(input("Сколько шагов пройдет робот{}?".format(robot2.name)))
robot2.motion()
robot2.recharge()

robot1.fight(robot2)
robot1.recharge()
robot2.recharge()
