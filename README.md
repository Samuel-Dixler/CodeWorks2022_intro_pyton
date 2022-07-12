# Project 5 Data Structures

## Lists

1) Given a list list1 = [100, 200, 300, 400, 500], reverse the order and save it as a new list

  list1.sort(reverse = True)

2) Write a program to add the lists below, index-wise. Create a new list that contains the 0th index item from both lists, then the 1st index item, and so on till the last element.
list1 = ["M", "na", "i", "Py"]
list2 = ["y", "me", "s", "thon"]

expected output
list3 = ['My', 'name', 'is', 'Python']

    list3 = [list1[0]+list2[0], list1[1]+list2[1], list1[2]+list2[2], list1[3]+list2[3]]

3) Given a list of numbers. write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]

  print(numbers[0]**2, numbers[1]**2, numbers[2]**2, numbers[3]**2, numbers[4]**2, numbers[5]**2, numbers[6]**2)

4) Concatenate two lists in the following order
list1 = ["Hello ", "Thank you "]
list2 = ["Dear", "Sir"]

list3 = ['Hello Dear', 'Hello Sir', 'Thank you  Dear', 'Thank you  Sir']

  list3 = [list1[0]+list2[0], list1[0]+list2[1], list1[1]+list2[0], list1[1]+list2[1]]


## Tuple

1) Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)

  IMPOSSIBLE

2) Counts the number of occurrences of item "the" from a tuple
tuple1 = ("the", "quick", "brown", "fox", "hit", "the", "road", "by", "the", "water")

  tuple1.count("the")

3)Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)

  tuple2 = (tuple1[3:-1])

## Sets
1) Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

  set3 = set1.union(set2)

2) Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

  set3 = set1.difference(set2)

3) Edit the file common.py so that it can check if two sets have any elements in common. If yes, display the common elements.
