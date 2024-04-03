# Andrew Butler     9-9-2022
# Program to check if a triangle is A) possible and B) if it is Equilateral, Isosceles, or Scalene.

# gathering side lengths from user
print("Enter the sidelengths of a triangle")
x = int( input("Enter an integer for side x: "))
y = int( input("Enter an integer for side y: "))
z = int( input("Enter an integer for size z: "))

# check to make sure that a traingle with the specified side lengths can exist
if (x + y > z) and (x + z > y) and (y + z > y):
    triangle = True
else:
    triangle = False
    print("Error: Triangle does not exist.")

# Check to see if the triangle is Equilateral, Isosceles, or Scalene, and prints what it finds
if (triangle == True) and (x == y == z):
    print("It is an Equilateral triangle.")
elif (triangle == True) and ((x == y) or (x == z) or (y == z)):
    print("It is an Isosceles triangle.")
elif (triangle == True):
    print("It is a Scalene triangle.")