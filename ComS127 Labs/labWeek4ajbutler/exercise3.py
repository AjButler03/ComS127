# Andrew Butler             9-16-22
# Lab Week 4 - Exercise #3



# Gathering x1, y1, x2, and y2 values from user
x1 = float( input("Enter a number for x1: "))
y1 = float( input("Enter a number for y1: "))
x2 = float( input("Enter a number for x2: "))
y2 = float( input("Enter a number for y2: "))

# figuring out if the line is vertical, horizontal, or the slope, and prints out result
if (x2 - x1) == 0:
    print("The line is vertical")
elif (y2 - y1)/(x2 - x1) == 0:
    print("The line is horizontal")
else:
    print("The slope of the line described by points ({0}, {1}) and ({2}, {3}) is {4}".format(x1, y1, x2, y2, ((y2 - y1)/(x2 - x1))))