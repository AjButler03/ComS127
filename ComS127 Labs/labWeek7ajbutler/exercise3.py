# Andrew Butler             10-06-2022
# Lab week 7 - Exercise #3

x = int( input("Enter an integer: "))

# outward slope
for i in range(0, x):
    for i in range(0, i+1):
        print("*", end="")
    print()

# inward slope
for i in range(-x+1, 0):
    for i in range(i, 0):
        print("#", end="")
    print()