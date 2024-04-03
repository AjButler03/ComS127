# Andrew Butler             10-20-2022
# Lab week 9 - exercise #2

import math

# takes in a list of x coordinates and list of y coordinates, and calculates their distance from a specific x,y coordinate. Outputs list of distances
def calculateDistance(listX, listY, x, y):
    listDistances = []
    for i in range (0, (len(listX))):
        distance = math.sqrt( ((listX[i] - x) ** 2) + ((listY[i] - y) ** 2) )
        listDistances.append(distance)
    return listDistances

def main():

    # Establishing lists
    listName = []
    listX = []
    listY = []

    # Taking input, appending lists
    while True:
        name = input("Enter city name (* to quit): ")
        if name == "*":
            break
        x = int( input("Enter X coordinate: "))
        y = int( input("Enter Y coordinate: "))
        listName.append(name)
        listX.append(x)
        listY.append(y)

    # taking input for current position
    x = int( input("Enter your X coordinate: "))
    y = int( input("Enter your Y coordinate: "))

    # finding distance from each city input above
    listDistances = calculateDistance(listX, listY, x, y)
    print(listName)
    print(listDistances)

    # printing out closest city and distance to it
    print()
    print("Closest location from ({0}, {1}): ".format(x, y))
    print(listName[ listDistances.index( min(listDistances) ) ])
    print(min(listDistances))

if __name__ == "__main__":
    main()