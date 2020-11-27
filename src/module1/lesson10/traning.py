class Human:
    def __init__(self, power, agility, iq, sex, health):
        self.power = power
        self.agility = agility
        self.iq = iq
        self.sex = sex
        self.health = health

    def skills(self):
        print("power = {}, agility = {}, iq = {}, sex = {}, health = {}".format(self.power, self.agility, self.iq,
                                                                                self.sex, self.health))

    def attack(self, other_human):
        other_human.health -= self.power

    def power_up(self, new_power):
        self.power += new_power

    def iq_battle(self, other_iq):
        if self.iq < other_iq:
            print("other_iq win")
        else:
            print("self win")

man1 = Human(30, 50, 89, "m", 100)
man1.skills()
man1.power_up(30)
man1.skills()
man2 = Human(50, 50, 100, "w", 120)
man2.skills()
man1.attack(man2)
man2.skills()
