import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_width
        self.build_tank()
        self.anim = []

    def build_tank(self):
        self.board = [self.board]
        for line in range(self.aqua_height - 1):
            self.board = self.board + [[' '] * self.aqua_width]
        for line in range(self.aqua_height):
            for column in range(self.aqua_width):
                if (column == 0 or column == self.aqua_width - 1) and (line != self.aqua_height - 1):
                    self.board[line][column] = '|'
                elif (column == 0) and (line == self.aqua_height - 1):
                    self.board[line][column] = '\\'
                elif (column == self.aqua_width - 1) and (line == self.aqua_height - 1):
                    self.board[line][column] = '/'
                elif (column != 0 or column != self.aqua_width - 1) and (line == 2):
                    self.board[2][column] = '~'
                elif (column != 0 and column != self.aqua_width - 1) and (line == self.aqua_height - 1):
                    self.board[line][column] = '_'

    def print_board(self):
        total = ''
        for line in range(self.aqua_height):
            for column in range(self.aqua_width):
                total = total + ' ' + self.board[line][column]
            total = total + '\n'
        print(total)

    def get_board(self):
        board = self.board
        return board

    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        return self.anim

    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        if not isinstance(animal, Crab.Crab):
            return False
        collision = False
        direction = Animal.Animal.get_directionH(animal)
        for crab in self.anim:
            if crab == self.anim[self.anim.index(animal)]:
                continue
            if isinstance(self.anim[self.anim.index(crab)], Crab.Crab):
                if direction:
                    if abs((crab.get_position()[0] - (animal.get_position()[0] + animal.get_size()[1]))) < 1:
                        collision = True
                        crab.set_directionH(1)
                        return collision
                elif not direction:
                    if abs((animal.get_position()[0] - (crab.get_position()[0] + crab.get_size()[1]))) < 1:
                        collision = True
                        crab.set_directionH(0)
                        return collision
        return collision

    def print_animal_on_board(self, animal: Animal):
        board = self.get_board()
        ani = animal.get_animal()
        for line in range(animal.y, animal.height + animal.y):
            if animal.y == self.aqua_height:
                line = line - MAX_CRAB_HEIGHT
                if len(ani) == 4:
                    line = line - 1
                    for column in range(animal.x, animal.width + animal.x):
                        board[line][column] = ani[(line + 1 + MAX_CRAB_HEIGHT - animal.y)][(column - animal.x)]
                else:

                    for column in range(animal.x, animal.width + animal.x):
                        board[line][column] = ani[(line + MAX_CRAB_HEIGHT - animal.y)][(column - animal.x)]
                continue
            for column in range(animal.x, animal.width + animal.x):
                board[line][column] = ani[(line - animal.y)][(column - animal.x)]
        return None

    def delete_animal_from_board(self, animal: Animal):
        board = self.get_board()
        ani = animal.get_animal()
        for line in range(animal.y, animal.height + animal.y):
            if animal.y == self.aqua_height:
                line = line - MAX_CRAB_HEIGHT
                if len(ani) == 4:
                    line = line - 1
                    for column in range(animal.x, animal.width + animal.x):
                        board[line][column] = ' '
                else:

                    for column in range(animal.x, animal.width + animal.x):
                        board[line][column] = ' '
                continue
            for column in range(animal.x, animal.width + animal.x):
                board[line][column] = ' '
        return None

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        """
        Adding fish to the aquarium
        """
        y1 = y
        if (x + MAX_ANIMAL_WIDTH) >= (self.aqua_width - 1):
            x = self.aqua_width - MAX_ANIMAL_WIDTH - 1
        if y >= (self.aqua_height - 2 - MAX_CRAB_HEIGHT):
            if fishtype == 'mo':
                y1 = self.aqua_height - 1 - MAX_CRAB_HEIGHT - MAX_ANIMAL_HEIGHT
            else:
                y1 = self.aqua_height - 1 - MAX_CRAB_HEIGHT - MAX_ANIMAL_HEIGHT
        if self.check_if_free(x, y1):
            if fishtype == 'mo':
                if y1 != y:
                    y = y1 + MAX_ANIMAL_HEIGHT - 3  # 3 for Moly height
                self.anim.append(Moly.Moly(name, age, x, y, directionH, directionV))
            else:
                if y1 != y:
                    y = y1 + MAX_ANIMAL_HEIGHT - 5  # 5 for Scalar height
                self.anim.append(Scalar.Scalar(name, age, x, y, directionH, directionV))
            self.print_animal_on_board(self.anim[-1])
            return True
        else:
            return False

    def add_crab(self, name, age, x, y, directionH, crabtype):
        """
        Adding crab to the aquarium
        """
        if x < (self.aqua_width - MAX_CRAB_WIDTH):
            if self.check_if_free(x, y):
                if crabtype == 'sh':
                    self.anim.append(Shrimp.Shrimp(name, age, x, y, directionH))
                else:
                    self.anim.append(Ocypode.Ocypode(name, age, x, y, directionH))
                self.print_animal_on_board(self.anim[-1])
                return True
            else:
                return False
        if (x + MAX_CRAB_WIDTH) >= (self.aqua_width - 1):
            x = self.aqua_width - MAX_CRAB_WIDTH - 1
            if self.check_if_free(x, y):
                if crabtype == 'sh':
                    self.anim.append(Shrimp.Shrimp(name, age, x, y, directionH))
                else:
                    self.anim.append(Ocypode.Ocypode(name, age, x, y, directionH))
                self.print_animal_on_board(self.anim[-1])
                return True
            else:
                return False

    def check_if_free(self, x, y) -> bool:
        """
        method for checking whether the position is empty before inserting a new animal
        """
        board = self.get_board()
        if y == self.aqua_height:
            y = y - MAX_CRAB_HEIGHT - 1
        if (x + MAX_CRAB_WIDTH) >= (self.aqua_width - 1):
            x = x - 1
        for line in range(y, y + MAX_ANIMAL_HEIGHT):
            if line == (self.aqua_height - 1):
                return True
            for column in range(x, x + MAX_ANIMAL_WIDTH):
                if board[line][column] != ' ':
                    print("The place is not available! please try again later.")
                    return False
        return True

    def left(self, a):
        if self.get_board()[(a.get_position()[1] - 2)][(a.get_position()[0] - 1)] == '|':
            self.delete_animal_from_board(a)
            a.set_directionH(1)
        elif isinstance(a, Crab.Crab) and (a.get_position()[0] >= 1) and self.is_collision(a):
            self.delete_animal_from_board(a)
            if self.get_board()[(a.get_position()[1] - 2)][(a.get_size()[1] + a.get_position()[0])] != '|':
                a.set_directionH(1)
                if not self.is_collision(a):
                    a.right()
        else:
            self.delete_animal_from_board(a)
            a.left()
        self.anim[self.anim.index(a)] = a
        self.print_animal_on_board(a)

    def right(self, a):
        if self.get_board()[(a.get_position()[1] - 2)][(a.get_size()[1] + a.get_position()[0])] == '|':
            self.delete_animal_from_board(a)
            a.set_directionH(0)
        elif isinstance(a, Crab.Crab) and (a.get_position()[0] <= (self.aqua_width - 1)) and self.is_collision(a):
            self.delete_animal_from_board(a)
            if self.get_board()[(a.get_position()[1] - 2)][(a.get_position()[0] - 1)] != '|':
                a.set_directionH(0)
                if not self.is_collision(a):
                    a.left()
        else:
            self.delete_animal_from_board(a)
            a.right()
        self.anim[self.anim.index(a)] = a
        self.print_animal_on_board(a)

    def up(self, a):
        self.delete_animal_from_board(a)
        if (a.get_position()[1]) == 3:
            a.set_directionV(0)
        else:
            a.up()
        self.anim[self.anim.index(a)] = a
        self.print_animal_on_board(a)

    def down(self, a):
        self.delete_animal_from_board(a)
        if (a.get_position()[1] + a.get_size()[0]) >= (self.aqua_height - MAX_CRAB_HEIGHT - 1):
            a.set_directionV(1)
        else:
            a.down()
        self.anim[self.anim.index(a)] = a
        self.print_animal_on_board(a)

    def next_turn(self):
        """
        Managing a single step
        """
        for animal in self.anim:
            if self.turn % 10 == 0 and self.turn >= 10:
                Animal.Animal.dec_food(animal)
                if self.turn % 100 == 0:
                    Animal.Animal.inc_age(animal)
            Animal.Animal.die(animal)
            Animal.Animal.starvation(animal)
            if Animal.Animal.get_food(animal) == 0 or Animal.Animal.get_age(animal) == 120:
                self.anim.remove(animal)
                Aqua.delete_animal_from_board(self, animal)
                continue
            if Animal.Animal.get_directionH(animal):
                Aqua.right(self, animal)
            else:
                Aqua.left(self, animal)
            if isinstance(animal, Fish.Fish):
                if Fish.Fish.get_directionV(animal):
                    Aqua.up(self, animal)
                else:
                    Aqua.down(self, animal)

        self.turn += 1

    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        for animal in self.anim:
            print(animal)

    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        for animal in self.anim:
            Animal.Animal.add_food(animal, FEED_AMOUNT)

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, y, directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:
        """
        Managing several steps
        """
        while True:
            n = (input("How many steps do you want to take?"))
            try:
                n = int(n)
            except ValueError:
                continue
            break

        for i in range(n):
            Aqua.next_turn(self)
        return None
