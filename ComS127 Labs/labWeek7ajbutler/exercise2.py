# Andrew Butler             10-06-2022
# Lab week 7 - Exercise #2

num = int( input("Enter an integer: "))
for i in range (0, num):
    for i in range(0, i+1):
        print(i, end="")
    print()