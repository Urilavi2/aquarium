import Fish


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.height = 3
        self.width = 8

    def get_animal(self):
        moly_style = [[' ', '*', '*', '*', ' ', ' ', ' ', '*'],
                      ['*', '*', '*', '*', '*', '*', '*', '*'],
                      [' ', '*', '*', '*', ' ', ' ', ' ', '*']]

        # MOLY_STYLE SWIMS LEFT
        moly_style_inverse = [[]]
        if self.directionH:
            for line in range(self.height):
                for column in range(self.width):
                    moly_style_inverse[line].append(moly_style[((self.height - 1) - line)][((self.width - 1) - column)])
                if line != self.height - 1:
                    moly_style_inverse.append([])

            return moly_style_inverse
        else:
            return moly_style
