# Сделать вот тут задание)))
# Наследование
# Родитель: класс Существо, дочение классы: человек, орк, эльф


class Thing:
    def __init__(self, name="", sex="", hp=0, mp=0, specialty="", race="Unknown", agility=0, strength=0, intellect=0):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.mp = mp
        self.specialty = specialty
        self.race = race
        self.agility = agility
        self.strength = strength
        self.intellect = intellect

    def info(self):
        print('''
                 Имя: {}
                 Пол: {}
                 Здоровье: {}
                 Мана: {}
                 Класс: {}
                 Раса: {}
                Характеристики:
                 Ловкость: {}
                 Сила: {}
                 Интеллект: {}\n'''.format(self.name, self.sex, self.hp, self.mp, self.specialty, self.race, self.agility,
                                        self.strength, self.intellect))

    def character_creating(self):
        self.name = input("Введите имя персонажа:")
        self.sex = input("Введите пол:")
        self.specialty = input("Выберите класс: Лучник, Воин, Маг \n")
        if self.specialty == "Лучник":
            self.hp = 100
            self.mp = 100
            self.agility += 100
        elif self.specialty == "Воин":
            self.hp = 200
            self.mp = 75
            self.strength += 100
        elif self.specialty == "Маг":
            self.hp = 75
            self.mp = 200
            self.intellect += 100
        else:
            print("Выбран случайный класс")
            self.hp = 75
            self.mp = 75


class Human(Thing):
    def __init__(self, name="", sex="", hp=0, mp=0, specialty="", race="Human", agility=0, strength=0, intellect=0, ):
        super().__init__(self, name="", sex="", hp=0, mp=0, specialty="",
                         race="Unknown", agility=0, strength=0, intellect=100)

    def character_creating(self):
        self.name = input("Введите имя персонажа:")
        self.sex = input("Введите пол:")
        self.specialty = input("Выберите класс: Лучник, Воин, Маг \n")
        if self.specialty == "Лучник":
            self.hp = 100
            self.mp = 100
            self.agility += 100
        elif self.specialty == "Воин":
            self.hp = 200
            self.mp = 75
            self.strength += 100
        elif self.specialty == "Маг":
            self.hp = 75
            self.mp = 200
            self.intellect += 100
        else:
            print("Выбран случайный класс")
            self.hp = 75
            self.mp = 75

    def info(self):
        print('''
                 Имя: {}
                 Пол: {}
                 Здоровье: {}
                 Мана: {}
                 Класс: {}
                Характеристики:
                 Ловкость: {}
                 Сила: {}
                 Интеллект: {}\n'''.format(self.name, self.sex, self.hp, self.mp, self.specialty, self.agility,
                                        self.strength, self.intellect))

class Elf(Thing):
    def __init__(self, name="", sex="", hp=0, mp=0, specialty="", race="Elf", spec="Pointy ears", agility=0, strength=0, intellect=0, ):
        super().__init__(name="", sex="", hp=0, mp=0, specialty="", race="Elf", agility=100, strength=0, intellect=0)
        self.spec = spec

    def character_creating(self):
        self.name = input("Введите имя персонажа:")
        self.sex = input("Введите пол:")
        self.specialty = input("Выберите класс: Лучник, Воин, Маг \n")
        if self.specialty == "Лучник":
            self.hp = 100
            self.mp = 100
            self.agility += 100
        elif self.specialty == "Воин":
            self.hp = 200
            self.mp = 75
            self.strength += 100
        elif self.specialty == "Маг":
            self.hp = 75
            self.mp = 200
            self.intellect += 100
        else:
            print("Выбран случайный класс")
            self.hp = 75
            self.mp = 75

    def info(self):
        print('''
                 Имя: {}
                 Пол: {}
                 Здоровье: {}
                 Мана: {}
                 Класс: {}
                 Особенность: {}
                Характеристики:
                 Ловкость: {}
                 Сила: {}
                 Интеллект: {}\n'''.format(self.name, self.sex, self.hp, self.mp, self.specialty, self.spec, self.agility,
                                        self.strength, self.intellect))



class Orc(Thing):
    def __init__(self, name="", sex="", hp=0, mp=0, specialty="", race="Orc", spec="Agressive", agility=0, strength=0, intellect=0, ):
        super().__init__(name="", sex="", hp=0, mp=0, specialty="", race="Orc", agility=0, strength=100, intellect=0)
        self.spec = spec

    def character_creating(self):
        self.name = input("Введите имя персонажа:")
        self.sex = input("Введите пол:")
        self.specialty = input("Выберите класс: Лучник, Воин, Маг \n")
        if self.specialty == "Лучник":
            self.hp = 100
            self.mp = 100
            self.agility += 100
        elif self.specialty == "Воин":
            self.hp = 200
            self.mp = 75
            self.strength += 100
        elif self.specialty == "Маг":
            self.hp = 75
            self.mp = 200
            self.intellect += 100
        else:
            print("Выбран случайный класс")
            self.hp = 75
            self.mp = 75

    def info(self):
        print('''
                 Имя: {}
                 Пол: {}
                 Здоровье: {}
                 Мана: {}
                 Класс: {}
                Характеристики:
                 Ловкость: {}
                 Сила: {}
                 Интеллект: {}\n'''.format(self.name, self.sex, self.hp, self.mp, self.specialty, self.agility,
                                        self.strength, self.intellect))


thing = Thing()
thing.character_creating()
thing.info()

elf = Elf()
elf.character_creating()
elf.info()

orc = Orc()
orc.character_creating()
orc.info()