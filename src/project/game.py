#define the class
class Character:
    #define the class variables
    characters = [{'name': 'Sam', 'level': 0, 'position': 0, 'lives': 3}, {'name': 'Lola', 'level': 0, 'position': 0, 'lives': 3}]

    players = ['Sam', 'Lola']

    currentPlayer = []

    #define the the init function
    def __init__(self, name):
        #your code here
        self.name = name


    def char(self):
        for x in Character.characters:
            if x['name'] == self.name:
                print("Now playing as " + self.name)
                print("\nWelcome back " + self.name + "!")
                break
            else:
                print("\nWelcome to the game, " + self.name + "!")
                Character.characters.append({'name': self.name, 'level': 0, 'position': 0, 'lives': 3})
                Character.players.append(self.name)
                break

        Character.currentPlayer = Character.characters[Character.players.index(self.name)]
        print(Character.currentPlayer)

    #add the methods
    def move():
        #your code here    position +/- x
        print("\n POSITION: " + str(Character.characters[Character.characters.index(Character.currentPlayer)]['position']))
        d = input("Which way: left or right?\n  Enter 1 for LEFT\n  Enter 2 for RIGHT\n  Enter 3 for RETURN TO MENU\n     ")
        o = Character.characters[Character.characters.index(Character.currentPlayer)]['position']
        if int(d) == 1:
            mL = input("How far to the left? ")
            Character.characters[Character.characters.index(Character.currentPlayer)]['position'] = int(o) - int(mL)
            print(Character.characters[Character.characters.index(Character.currentPlayer)]['position'])

        elif int(d) == 2:
            mR = input("How far to the right? ")
            Character.characters[Character.characters.index(Character.currentPlayer)]['position'] = int(o) + int(mR)
            print(Character.characters[Character.characters.index(Character.currentPlayer)]['position'])

        elif int(d) == 3:
            print("   Returning to MENU")
        else: print("Invalid Option. Returning to MENU")


    def level_up():
        #your code here   level + 1
        print("\n LEVEL: " + str(Character.characters[Character.characters.index(Character.currentPlayer)]['level']))
        li = input("  Enter 1 to LEVEL-UP\n  Enter 0 for RETURN TO MENU\n     ")
        lvl = Character.characters[Character.characters.index(Character.currentPlayer)]['level']
        if int(li) == 1:
            Character.characters[Character.characters.index(Character.currentPlayer)]['level'] = int(lvl) + 1
            print(Character.characters[Character.characters.index(Character.currentPlayer)]['level'])

        elif int(li) == 0:
            print("   Returning to MENU")
        else: print("Invalid Option. Returning to MENU")


    def kill():
        #your code here    lives - 1
        print("\n LIVES: " + str(Character.characters[Character.characters.index(Character.currentPlayer)]['lives']))
        di = input("  Enter 1 to DIE\n  Enter 0 for RETURN TO MENU\n     ")
        die = Character.characters[Character.characters.index(Character.currentPlayer)]['lives']
        if int(di) == 1:
            Character.characters[Character.characters.index(Character.currentPlayer)]['lives'] = int(die) - 1
            print(Character.characters[Character.characters.index(Character.currentPlayer)]['lives'])

        elif int(li) == 0:
            print("   Returning to MENU")
        else: print("Invalid Option. Returning to MENU")

    def bonus():
        #your code here   lives + 1
        print("\n LIVES: " + str(Character.characters[Character.characters.index(Character.currentPlayer)]['lives']))
        bi = input("  Enter 1 to ADD BONUS LIVES\n  Enter 0 for RETURN TO MENU\n     ")
        bon = Character.characters[Character.characters.index(Character.currentPlayer)]['lives']
        if int(bi) == 1:
            bn = input("How many bonus lives do you want to add?  ")
            Character.characters[Character.characters.index(Character.currentPlayer)]['lives'] = int(bon) + int(bn)
            print(Character.characters[Character.characters.index(Character.currentPlayer)]['lives'])

        elif int(bi) == 0:
            print("   Returning to MENU")
        else: print("Invalid Option. Returning to MENU")

    def view():
        print("")
        for x in Character.characters:
            print("PLAYER NAME: " + str(x['name']) + "   " + "LEVEL: " + str(x['level']) + "   " + "POSITION: " + str(x['position']) + "   " + "LIVES: " + str(x['lives']))


#create 4 instance of this class and test all the methods
run = True
while run:
    choice = input("\nEnter 1 to PLAY \nEnter 2 to VIEW PLAYER LIST \nEnter 0 to QUIT\n  ")
    if int(choice) == 0:
        run = False
        break

    elif int(choice) == 1:
        p1 = Character(input("Enter PLAYER NAME:\n  "))
        p1.char()

        run_2 = True
        while run_2:
            choice_2 = input("\nWhat do you want to do?\n  Enter 1 to MOVE\n  Enter 2 to LEVEL-UP\n  Enter 3 to DIE\n  Enter 4 to ADD LIvES\n  Enter 9 to RETURN TO MENU\n  Enter 0 to QUIT\n  ")
            if int(choice_2) == 0:
                run_2 = False
                run = False
                break

            elif int(choice_2) == 1:
                Character.move()

            elif int(choice_2) == 2:
                Character.level_up()

            elif int(choice_2) == 3:
                Character.kill()

            elif int(choice_2) == 4:
                Character.bonus()

            elif int(choice_2) == 9:
                break
            else: print("Invalid option! Try again.")


    elif int(choice) == 2:
        Character.view()

    else: print("Invalid option! Try again.")


Character.view()
