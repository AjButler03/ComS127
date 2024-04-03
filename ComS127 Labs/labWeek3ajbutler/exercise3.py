# Andrew Butler     9-9-2022
# Lab week 3 - exercise #3
import math


# gathering values for a, b, and c from user
a = int( input("Enter an integer (A): "))
b = int( input("Enter another integer (B): "))
c = int( input("Enter another integer (C) that is not 0, and is not equal to the first one: "))
abc = (a, b, c)

# Printing various basic math functions
print("Sum of the 3 integers:", (a + b + c))
print("Modulus A mod C:", (a%c))
print("A times B, divided by C:", ((a*b)/c))
x = c-a
print("C minus A = X, then C divided by X:", (c/x))
print("Average of A, B, and C:", ((a + b + c)/3))