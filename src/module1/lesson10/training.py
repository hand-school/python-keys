import random


class Characters:
    def __init__(self, name, dmg, defence, max_hp):
        self.name = name
        self.dmg = dmg
        self.hp = max_hp
        self.defence = defence

    def hit(self, character):
        character.hp -= (self.dmg - character.defence) * random.uniform(0.75, 1.15)
        print(character.name + ' пизданул по ' + character.name)

    def miss(self, character):
        character.hp -= (self.dmg - character.defence) * random.uniform(0.75, 1.15)


class Human(Characters):

    def __init__(self, name='Olegator', dmg=3, max_hp=100, defence=0, mana=100):
        super().__init__(name, dmg, defence, max_hp)
        self.mana = mana

    def buff(self, heal):
        if self.mana >= 25:
            self.hp += heal
            self.mana -= 25
            print(' ~Господи, похилимся!!~ ')
        else:
            print(' ~Ой... Маны нет!~ ')

    def info(self):
        print()


class Ogre(Characters):

    def __init__(self, name='AlexMeister', dmg=4, defence=3, max_hp=100):
        super().__init__(name, dmg, defence, max_hp)

