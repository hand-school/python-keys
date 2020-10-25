import random


class Characters():
    def __init__(self, name, dmg, max_hp=100):
        self.name = name
        self.dmg = dmg
        self.hp = max_hp



class Human(Characters):


    def __init__(self, name, dmg, max_hp=100, defence=0, mana=100):
        super.__init__(self,name, dmg, max_hp=100)
        self.name = name
        self.dmg = dmg
        self.hp = max_hp
        self.mana = mana
        self.defence = defence

    def hit(self, character):
        character.hp -= (self.dmg - self.defence) * random.uniform(0.75, 1.15)
        print(character.name + ' пизданул по ' + character.name)

    def buff(self, heal):
        if self.mana >= 25:
            self.hp += heal
            self.mana -= 25
            print(' ~Господи, похилимся!!~ ')
        else:
            print(' ~Маны нет!~ ')

    def use_hp(self):
        if self.heal_potion > 0:
            self.hp += 50
            self.heal_potion -= 1
            print(self.hp)
        else:
            print(' Ой... Нет хилок! ')

    def info(self):
        print()


class Ogre(Characters):

    def __init__(self, name, dmg, max_hp=100, defence=3):
        super().__init__(name, name, dmg, max_hp=100)
        self.name = name
        self.dmg = dmg
        self.hp = max_hp
        self.defence = defence


