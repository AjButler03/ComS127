# Andrew Butler     9-9-2022
# Lab week 3 - Exercise #2
from cmath import pi
import math

# getting radius from user
circ_radius = int( input("Enter an integer for radius: "))

#finding area and volume given radius
circ_area = 4 * pi * (circ_radius ** 2)
circ_vol = (4 * pi * (circ_radius ** 3))/3

# printing results
print("The area of the sphere is {0},".format(circ_area),
    "and the volume of the sphere is {0}.".format(circ_vol))