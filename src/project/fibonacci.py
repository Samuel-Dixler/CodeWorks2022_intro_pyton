list = [0,1]

def fib(n):
    while int(n) > len(list):
        list.append(int(list[-1]) + int(list[-2]))

fib(input("How many Fibonacci Numbers do you want? "))
print(list)
