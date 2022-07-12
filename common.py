set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set3 = set1.intersection(set2)

print(set1)
print(set2)
print(set3)

if bool(set3) == False :
  print("Two sets have no items in common")
else:
  print("Two sets have items in common: ", set3)
