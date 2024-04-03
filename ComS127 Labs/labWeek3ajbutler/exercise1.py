# Andrew Butler     9-9-2022
# Lab Week 3 - Exercise #1

import math

# gathering sidelengths from user
a = float( input("Enter an integer for sidelength a: "))
b = float( input("Enter an integer for sidelength b: "))
c = float( input("Enter an integer for sidelength c: "))

s = (a+b+c)/2

# calculating area of triangle, given sidelengths and calculated s
area_triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))

# printing result
print("Area of the triangle is {0}".format(area_triangle))