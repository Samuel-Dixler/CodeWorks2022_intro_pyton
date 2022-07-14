import re

a = input("Enter a word: ")
x = re.sub("[aeiou]", "", a)
print(x)
