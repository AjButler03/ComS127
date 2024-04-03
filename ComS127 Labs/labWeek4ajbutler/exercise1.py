# Andrew Butler             9-15-2022
# Lab Week 4 - Exercise #1


# Gather length/height from user
length = float( input("Enter the length of the rectangle: "))
height = float( input("Enter the height of the rectangle: "))

# Determine perimeter
perimeter = 2 * (length + height)

# Determining if the rectangle is square and printing final result
if length == height:
    print("This rectangle is square with a perimeter of {0}".format(perimeter))
else:
    print("The perimeter of this rectangle is {0}".format(perimeter))