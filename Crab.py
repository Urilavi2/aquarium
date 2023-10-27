import Animal

MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7


class Crab(Animal.Animal):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = MAX_CRAB_WIDTH
        self.height = MAX_CRAB_HEIGHT

    def __str__(self):
        st = "the crab " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st

    def starvation(self):
        st = "The crab " + str(self.name) + " died a the age of " + str(self.age) + " years because he ran out of food!"
        if self.food == 0:
            print(st)

    def die(self):
        if self.age == 120:
            self.alive = False
            st = str(self.name) + " died in good health"
            return st
