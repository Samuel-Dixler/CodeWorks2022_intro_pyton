#User account managment
class bcolors:
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

users = [{'user_name': 'Sam', 'email': 'dixler.inc', 'password': 'abc'}, {'user_name': 'Lola', 'email': 'lola123', 'password': 'efg'}]


def create_user(user_name, email, password1, password2):
    #YOUR CODE HERE
    for x in users:
        if x['email'] == email:
            print(f"{bcolors.RED}Error: Email already in use! Sign-up failed. Try again later{bcolors.RESET}")
            break
    else:
        if password1 != password2:
            print(f"{bcolors.RED}Error: Password doesn't match! Sign-up failed. Try again later{bcolors.RESET}")
        else:
            print(f"{bcolors.GREEN} >--< Welcome " + user_name + f"! >--< {bcolors.RESET}")
            users.append({'user_name': user_name, 'email': email, 'password': password1})

def get_user(email):
    for x in users:
        if x['email'] == email:
            print("Username: " + x['user_name'] + "   Email: " + x['email'] + "   Password: " + x['password'])
            break
    else:
        print(f"{bcolors.RED}Error: Email not in use. Try again later.{bcolors.RESET}")

def get_all_users():
    for x in users:
        print("Username: " + x['user_name'] + "   Email: " + x['email'] + "   Password: " + x['password'])

    #YOUR CODE HERE

run = True
while run:
    choice = input(f"{bcolors.GREEN}\n >--< Welcome to the User-Email Database >--< {bcolors.RESET}\n   Enter {bcolors.GREEN}1{bcolors.RESET} to Sign-Up \n   Enter {bcolors.GREEN}2{bcolors.RESET} to Search for User by Email \n   Enter {bcolors.GREEN}3{bcolors.RESET} to View List of Users \n   Enter {bcolors.GREEN}0{bcolors.RESET} to Exit \n    ")


    if int(choice) == 0:
        run = False
        break

    elif int(choice) == 1:
        create_user(user_name = input("Enter Username: "), email = input("Enter Email: "), password1 = input("Create Password: "), password2 = input("Re-Enter Password: "))

    elif int(choice) == 2:
        get_user(input("\n >--< User Search >--< \n     Enter an Email\n   "))

    elif int(choice) == 3:
        get_all_users()

    else:
        print(f"{bcolors.RED}\n Invalid Option. Please try again.{bcolors.RESET}")





#Testing the Code

## try creating three new users and print out the results

## Try adding one of the three users you added and print out the results

## Try adding a new user with passwords that don't matches and print out the results

## Get the second users print out their user name and email

## Get all users and print only their user names
