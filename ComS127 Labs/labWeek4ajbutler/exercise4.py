# Andrew Butler             9-16-2022
# Lab Week 4 - Exercise #4
import math

# Gathering m1 and m2 values from user
m1 = float( input("Enter a float value for m1: "))
m2 = float( input("Enter a float value for m2: "))

# figuring out if m1 and m2 are parallel, perpendicular, or finding the angle between them, and printing result
if m1 == m2:
    print("Slope m1 and slope m2 are parallel ({0})".format(m1))
elif (m1 == (-1/m2)) or (m2 == -1/m2):
    print("Slopes m1 ({0}) and m2 ({1}) are perpendicular".format(m1, m2))
else:
    angle = math.atan((m1-m2)/(1+ m1 * m2))
    angle = math.degrees(angle)
    print("The angle between slopes m1 ({0}) and m2 ({1}) is {2} degrees.".format(m1, m2, angle))