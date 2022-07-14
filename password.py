password = "abcdefg"
attemptCount = 0

while attemptCount < 3:
    a = input("Enter your password: ")
    if a == password:
        break
    else:
        print("Password is incorrect. Please try again.")
        attemptCount += 1
        print(attemptCount)
if attemptCount == 3:
    print("Access Denied")
else:
    print("Welcome")
