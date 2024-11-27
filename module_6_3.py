class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self):
        self._cords = [5, 5, 25]
        self.speed = 0

    def move(self, dx, dy, dz):
        self.x = self._cords[0] + dx * self.speed
        self.y = self._cords[1] + dy * self.speed
        self.z = self._cords[2] + dz * self.speed
        self.z_ = self.z
        if self.z < 0:
            self.x = self._cords[0]
            self.y = self._cords[1]
            self.z = self._cords[2]
            print('It`s too deep, I can`t dive')

    def get_cords(self):
        print(f'X: {self.x} Y: {self.y} Z: {self.z}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print('Be careful, i`m attacking you 0_0')

import random
class Bird(Animal):
    beak = True
    def lay_eggs(self):
        a = random.choice([1,2,3,4])
        print(f"Here are(is) {a} eggs for you")

class Aquatic(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.z = self.z_ - abs(dz) * (self.speed / 2)

class Poisonous(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, Poisonous, Aquatic):
    sound = 'Click-click-click'
    def __init__(self, speed):
        super().__init__()
        self.speed = speed

db = Duckbill(4)
print(db.live)
print(db.beak)
print(db.sound)
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(-18)
db.get_cords()
db.lay_eggs()






