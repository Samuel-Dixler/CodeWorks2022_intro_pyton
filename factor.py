list =  []

for x in range(2000,3201):
    if x%7 == 0:
        if x%5 == 0:
            pass
        else:
            list.append(x)
print(list)
