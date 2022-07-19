one = input("Enter a number: ")
two = input("Enter another number: ")
list = []

if int(one) <= int(two):
    for x in range(int(one), int(two)+1):
        if x%2 == 0:
            pass
        else:
            list.append(x)
else:
    for x in range(int(two), int(one)+1):
        if x%2 == 0:
            pass
        else:
            list.append(x)

print(list)
