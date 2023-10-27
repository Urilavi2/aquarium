import Fish


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 5

    def get_animal(self):
        scalar_style = [['*', '*', '*', '*', '*', '*', ' ', ' '],
                        [' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                        [' ', ' ', '*', '*', '*', '*', '*', '*'],
                        [' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                        ['*', '*', '*', '*', '*', '*', ' ', ' ']]
        #SCALAR_STYLE SWIMS RIGHT
        scalar_style_inverse = [[]]
        if self.directionH:
            return scalar_style
        else:
            for line in range(self.height):
                for column in range(self.width):
                    scalar_style_inverse[line].append(scalar_style[((self.height - 1) - line)]
                                                      [((self.width - 1) - column)])
                if line != self.height - 1:
                    scalar_style_inverse.append([])

            return scalar_style_inverse

