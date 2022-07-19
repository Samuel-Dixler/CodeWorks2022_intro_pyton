player = {
    'name': 'Player 1',
    'position': 0,
    'direction': 'right'
}

#Your code here

def move(direction, speed):
    if direction == 'left':
        player['position'] = player['position'] - speed
    elif direction == 'right':
        player['position'] = player['position'] + speed
    return player['position']

player['name'] = input("What should I call you? ")

run_code = True
while run_code:
    user_input = int(input("\nWhat do you want to do, " + player['name'] + "?\nEnter 1 to move left\nEnter 2 to move right\nEnter 3 to exit\n"))
    #Your code here

    if user_input == 1:
        user_input = int(input("How far to the left? "))
        print("Updated " + player['name'] + " Position: " + str(move('left', user_input)))

    elif user_input == 2:
        user_input = int(input("How far to the right? "))
        print("Updated " + player['name'] + " Position: " + str(move('right', user_input)))

    elif user_input == 3:
        print("Good Bye!")
        run_code = False
