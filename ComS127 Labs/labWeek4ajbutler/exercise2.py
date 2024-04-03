# Andrew Butler             9-15-2022
# Lab Week 4 - Exercise #2

# Gathering values for a, b, c, x, and y from user
print("ax^2 + bx + c")
a = float( input("Enter a number for a: "))
b = float( input("Enter a number for b: "))
c = float( input("Enter a number for c: "))
x = float( input("Enter a number for x coordinate(x): "))
y = float( input("Enter a number for y coordinate(y): "))


# checking if the user-specified point lies on the user-specified parabola, and printing result
if a * x ** 2 + b * x + c == y:
    print("The point {0}, {1} lies on the parabola described by the equation y = {2} * x ** 2 + {3} * x + {4}".format(x, y, a, b, c))
else:
    print("The point {0}, {1} does not lie on the parabola described by the equation y = {2} * x ** 2 + {3} * x + {4}".format(x, y, a, b, c))