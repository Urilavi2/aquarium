import time
import Aqua
import Fish


def is_valid_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True


def demo(myaqua):

    myaqua.add_animal("scalarfish1", 4, 10, 10, 1, 0, 'sc')
    myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo')
    myaqua.add_animal("shrimpcrab1", 3, 20, myaqua.aqua_height, 1, 0, 'sh')
    myaqua.add_animal("ocypodecrab2", 13, 41, myaqua.aqua_height, 0, 0, 'oc')
    myaqua.print_board()

    for i in range(120):
        for animal in myaqua.get_all_animal():
            if i % 10 == 0 and i >= 10:
                animal.dec_food()
                if i % 100 == 0:
                    animal.inc_age()
            if (i % 30 == 0) and (i < 100):
                animal.add_food(10)
            animal.die()
            animal.starvation()
            if animal.get_food() == 0 or animal.get_age() == 120:
                myaqua.get_all_animal().remove(animal)
                myaqua.delete_animal_from_board(animal)
                continue
            if animal.get_directionH():
                myaqua.right(animal)
            else:
                myaqua.left(animal)
            if isinstance(animal, Fish.Fish):
                if animal.get_directionV():
                    myaqua.up(animal)
                else:
                    myaqua.down(animal)
        time.sleep(0.5)
        myaqua.print_board()


def add_animal(myaqua):
    choice = 0
    while not 1 <= choice <= 4:
        print("Please select:")
        print("1. Scalare")
        print("2. Moly")
        print("3. Ocypode")
        print("4. Shrimp")
        choice = input("What animal do you want to put in the aquarium?")
        if is_valid_int(choice):
            choice = int(choice)
        else:
            choice = 0

    name = input("Please enter a name:")
    while name == '':
        name = input("Please enter a name:")
    age = 0
    while not 1 <= age <= 100:
        age = input("Please enter age:")
        if is_valid_int(age):
            age = int(age)
        else:
            age = 0

    success = False
    while not success:
        x, y = 0, 0
        while not 1 <= x <= (myaqua.aqua_width - 1):
            x = input("Please enter an X axis location (1 - %d):" % (myaqua.aqua_width - 1))
            if is_valid_int(x):
                x = int(x)
            else:
                x = 0
        if choice == 1 or choice == 2:
            while not Aqua.WATERLINE <= y <= (myaqua.aqua_height - 1):
                y = input("Please enter an Y axis location (%d - %d):" % (Aqua.WATERLINE, myaqua.aqua_height - 1))
                if is_valid_int(y):
                    y = int(y)
                else:
                    y = 0

        directionH, directionV = -1, -1
        while not (directionH == 0 or directionH == 1):
            directionH = input("Please enter horizontal direction (0 for Left, 1 for Right):")
            if is_valid_int(directionH):
                directionH = int(directionH)
            else:
                directionH = -1
        if choice == 1 or choice == 2:
            while not (directionV == 0 or directionV == 1):
                directionV = input("Please enter vertical direction  (0 for Down, 1 for Up):")
                if is_valid_int(directionV):
                    directionV = int(directionV)
                else:
                    directionV = -1

        if choice == 1:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'sc')
        elif choice == 2:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'mo')
        elif choice == 3:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height, directionH, 0, 'oc')
        else:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height, directionH, 0, 'sh')
    return None


if __name__ == '__main__':
    width = 0
    height = 0
    
    print('Welcome to "The OOP Aquarium"')
    while width < 40:
        width = input("The width of the aquarium (Minimum 40): ")
        if is_valid_int(width):
            width = int(width)
        else:
            width = 0
    while height < 25:
        height = input("The height of the aquarium (Minimum 25): ")
        if is_valid_int(height):
            height = int(height)
        else:
            height = 0
    myaqua = Aqua.Aqua(width, height)

    while True:
        choice = 0
        while not 1 <= choice <= 7:
            print("Main menu")
            print("-"*30)
            print("1. Add an animal")
            print("2. Drop food into the aquarium")
            print("3. Take a step forward")
            print("4. Take several steps")
            print("5. Demo")
            print("6. Print all")
            print("7. Exit")

            choice = input("What do you want to do?")
            if is_valid_int(choice):
                choice = int(choice)
            else:
                choice = 0

        if choice == 1:
            add_animal(myaqua)
        elif choice == 2:
            myaqua.feed_all()
        elif choice == 3:
            myaqua.next_turn()
        elif choice == 4:
            myaqua.several_steps()
        elif choice == 5:
            demo(myaqua)
        elif choice == 6:
            myaqua.print_all()
        else:
            print("Bye bye")
            exit()

        myaqua.print_board()

