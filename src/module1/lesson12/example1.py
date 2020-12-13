class Parent:

    def __init__(self, hair_color, skin_color, sex, race, eyes_color):
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.sex = sex
        self.race = race
        self.eyes_color = eyes_color

    def fuck(self, other_parent):
        import random
        hair_color_rand = self.hair_color if random.randint(0, 1) else other_parent.hair_color
        skin_color_rand = self.skin_color if random.randint(0, 1) else other_parent.skin_color
        sex_rand = self.sex if random.randint(0, 1) else other_parent.sex
        race_rand = self.race if random.randint(0, 1) else other_parent.race
        eyes_color_rand = self.eyes_color if random.randint(0, 1) else other_parent.eyes_color

        return Child(hair_color_rand, skin_color_rand, sex_rand, race_rand, eyes_color_rand)

    def work(self):
        print("Оооо я работаю")


class Child(Parent):

    def __init__(self, hair_color, skin_color, sex, race, eyes_color, weight=10):
        super().__init__(hair_color, skin_color, sex, race, eyes_color)
        self.weight = weight

    def work(self):
        print("Я ребенок, я не работаю!")

    def parent_work(self):
        super().work()


parent1 = Parent("black", "white", 'male', 'human', 'blue')
parent2 = Parent("red", "white", 'female', 'human', 'green')

child = parent1.fuck(parent2)
child.work()
