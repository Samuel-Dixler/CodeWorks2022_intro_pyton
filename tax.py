num1 = int(input("Enter your annual income: "))

if num1 > 0 and num1 <=9950:
    print("You're in the 1st bracket. you will pay "+ str(num1 * (0.1)) + " in taxes")
elif num1 > 9951 and num1 <=40525:
    print("You're in the 2nd bracket. you will pay "+ str(num1 * (0.12)) + " in taxes")
elif num1 > 40526 and num1 <=86375:
    print("You're in the 3rd bracket. you will pay "+ str(num1 * (0.22)) + " in taxes")
elif num1 > 86375:
    print("You're in the 4th bracket. you will pay "+ str(num1 * (0.4)) + " in taxes")
else:
    print("The number you entered is not recognized")
