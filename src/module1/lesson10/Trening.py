class Dog:
    def __init__(self, sex, breed, colour, size, health='good'):
        self.sex = sex
        self.breed = breed
        self.colour = colour
        self.size = size
        self.health = health
        self.value = None

    def copulation(self, partner):
        if self.sex == "female" and partner.sex == "male":
            return Dog(self.sex, partner.breed, self.colour + "_" + partner.colour, partner.size, self.health)
        elif self.sex == "male" and partner.sex == "female":
            return Dog(partner.sex, self.breed, partner.colour + "_" + self.colour, self.size, partner.health)
        else:
            print("nonononono")

    def dog_show(self):
        if self.health == "good" and self.breed != "mongrel":
            self.value = "income"
        else:
            self.value = "useless"

    def medical_examination(self):
        if self.value == None:
            return ("sex = {}, breed = {}, colour = {}, size = {}, health = {}".format(self.sex, self.breed, self.colour,
                                                                                     self.size, self.health))
        else:
            return ("sex = {}, breed = {}, colour = {}, size = {}, health = {}, value = {}".format(self.sex, self.breed,
                                                                                                 self.colour,
                                                                                                 self.size, self.health,
                                                                                                 self.value))


dog1 = Dog("male", "chihuahua", "black", "little", "ill")
dog2 = Dog("female", "shepherd", "orange", "big")
dog3 = Dog(sex="male", breed="husky", colour="white", size="big", health="old")

puppy = dog1.copulation(dog2)
puppy1 = dog2.copulation(dog3)

dog1.copulation(dog3)

print(puppy.medical_examination())
print(puppy1.medical_examination())

print(dog1.medical_examination())
print(dog2.medical_examination())
print(dog3.medical_examination())

dog1.dog_show()
dog2.dog_show()
dog3.dog_show()

print(dog1.medical_examination())
print(dog2.medical_examination())
print(dog3.medical_examination())


