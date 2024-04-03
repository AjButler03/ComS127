# Andrew Butler             10-06-2022
# Lab week 7 - Exercise #1

x = str( input("Enter a string: "))
num = 0
for letter in x:
    num += 1
print("There are {0} characters in '{1}'".format(num, x))