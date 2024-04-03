# Andrew Butler          7-7-2022
# Conditional Logic Demo

val1 = int( input("Enter an Integer for val1: "))
val2 = int( input("enter an Integer for val2: "))

if val1 <= val2:
    print("The value of val1, {0}, is <= val2, {1}.".format(val1, val2))
else:
    print("The value of val1, {0}, is > val2, {1}.".format(val1, val2))