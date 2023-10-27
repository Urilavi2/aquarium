import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 3

    def get_animal(self):
        shrimp_style = [['*', ' ', '*', ' ', ' ', ' ', ' '],
                        [' ', '*', '*', '*', '*', '*', '*'],
                        [' ', ' ', '*', ' ', '*', ' ', ' ']]
        shrimp_style_inverse = [[]]
        if not self.directionH:
            return shrimp_style
        else:
            for line in range(self.height):
                for column in range(self.width):
                    shrimp_style_inverse[line].append(shrimp_style[line]
                                                      [((self.width - 1) - column)])
                if line != self.height - 1:
                    shrimp_style_inverse.append([])

            return shrimp_style_inverse
        return shrimp_style
