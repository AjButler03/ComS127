# Matthew Holman              10-15-2022
# Forest Escape game

import random
import colorama

def createRawMaze(piece, mazeWidth, mazeHeight):
    maze = []
    for i in range(0, mazeHeight):
        maze.append([])
        for j in range(0, mazeWidth):
            maze[i].append(piece)

    return maze

def renderMaze(maze):
    for row in maze:
        for item in row:
            if item == "#":
                print(colorama.Fore.LIGHTGREEN_EX + colorama.Back.GREEN + item, end="")
            elif item == "@":
                print(colorama.Fore.BLUE + item, end="")
            elif item == "E":
                print(colorama.Fore.LIGHTYELLOW_EX + colorama.Back.YELLOW + item, end="")
            elif item == ".":
                print(colorama.Fore.YELLOW + item, end="")
            else:
                print(item, end="")
        print()

def selectRandomNeighbor(currentCell, mazeWidth, mazeHeight, maze):
    chosenCell = None
    neighborChoice = random.randint(0, 3)
    if neighborChoice == 0 and (currentCell[1]+2 < mazeHeight   and maze[currentCell[1]+2][currentCell[0]] == "#"):
        chosenCell = (currentCell[0], currentCell[1]+2)
    elif neighborChoice == 1 and (currentCell[1]-2 >= 0         and maze[currentCell[1]-2][currentCell[0]] == "#"):
        chosenCell = (currentCell[0], currentCell[1]-2)
    elif neighborChoice == 2 and (currentCell[0]+2 < mazeWidth  and maze[currentCell[1]][currentCell[0]+2] == "#"):
        chosenCell = (currentCell[0]+2, currentCell[1])
    elif neighborChoice == 3 and (currentCell[0]-2 >= 0         and maze[currentCell[1]][currentCell[0]-2] == "#"):
        chosenCell = (currentCell[0]-2, currentCell[1])
    
    return chosenCell

def genMaze(x, y, mazeWidth, mazeHeight, maze):
    # CITATION: https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_depth-first_search (Iterative implementation)

    stack = []
    currentCell = None

    # Choose an starting cell and mark it as 'visited'
    maze[y][x] = "."

    # Push the newly marked cell to the stack
    stack.append((x, y))

    # Run while the stack is not empty
    while len(stack) > 0:
        # Pop the topmost cell off of the stack and assign it to be the currentCell
        currentCell = stack.pop()

        # Check for unmarked neighbors
        if ((currentCell[1]+2 < mazeHeight and maze[currentCell[1]+2][currentCell[0]] == "#") or
            (currentCell[1]-2 >= 0         and maze[currentCell[1]-2][currentCell[0]] == "#") or
            (currentCell[0]+2 < mazeWidth  and maze[currentCell[1]][currentCell[0]+2] == "#") or
            (currentCell[0]-2 >= 0         and maze[currentCell[1]][currentCell[0]-2] == "#")):
            
            # If there is an unmarked neighbor, push the current cell onto the stack
            stack.append(currentCell)

            # Select one of currentCell's unvisited neighbors and assign it to chosenCell
            chosenCell = selectRandomNeighbor(currentCell, mazeWidth, mazeHeight, maze)
            while chosenCell == None:
                chosenCell = selectRandomNeighbor(currentCell, mazeWidth, mazeHeight, maze)

            # Delete the wall between currentCell and chosenCell
            if currentCell[0] > chosenCell[0]:
                maze[currentCell[1]][currentCell[0]-1] = "."
            elif currentCell[0] < chosenCell[0]:
                maze[currentCell[1]][currentCell[0]+1] = "."
            elif currentCell[1] > chosenCell[1]:
                maze[currentCell[1]-1][currentCell[0]] = "."
            elif currentCell[1] < chosenCell[1]:
                maze[currentCell[1]+1][currentCell[0]] = "."

            # Delete the chosen cell from the maze and push its coordinates on to the stack
            maze[chosenCell[1]][chosenCell[0]] = "."
            stack.append(chosenCell)
    
    return maze

def genRooms(numRooms, roomMin, roomMax, mazeWidth, mazeHeight, maze):
    for i in range(0, numRooms):
        roomStartX = random.randint(1, mazeWidth-2)
        roomStartY = random.randint(1, mazeHeight-2)
        roomSizeX = random.randint(roomMin, roomMax)
        roomSizeY = random.randint(roomMin, roomMax)

        # 012345678
        #       X---
        if roomStartX + roomSizeX > mazeWidth-1:
            roomSizeX = mazeWidth - roomStartX-1
        if roomStartY + roomSizeY > mazeHeight-1:
            roomSizeY = mazeHeight - roomStartY-1

        for j in range(0, roomSizeY):
            for k in range(0, roomSizeX):
                maze[roomStartY+j][roomStartX+k] = "."
    
    return maze

def initMaze(mazeWidth, mazeHeight):

    maze = createRawMaze("#", mazeWidth, mazeHeight)
    maze = genMaze(1, 1, mazeWidth, mazeHeight, maze)
    maze = genRooms(10, 5, 9, mazeWidth, mazeHeight, maze)

    return maze

def initGamePiece(piece, mazeWidth, mazeHeight, maze):
    pieceStats = []

    pieceX = random.randint(1, mazeWidth-2)
    pieceY = random.randint(1, mazeHeight-2)
    
    while maze[pieceY][pieceX] != ".":
        pieceX = random.randint(1, mazeWidth-2)
        pieceY = random.randint(1, mazeHeight-2)

    maze[pieceY][pieceX] = piece

    pieceStats.append(pieceX)
    pieceStats.append(pieceY)

    return pieceStats # [pieceX, piecetY]

def playerMovement(playerInput, playerStats, playerEnergy, maze, forest):
    if playerInput == "n" and maze[playerStats[1]-1][playerStats[0]] == "." or maze[playerStats[1]-1][playerStats[0]] == "E":
        maze[playerStats[1]][playerStats[0]] = "." 
        maze[playerStats[1]-1][playerStats[0]] = "@"
        forest[playerStats[1]][playerStats[0]] = "." 
        forest[playerStats[1]-1][playerStats[0]] = "@"
        playerStats[1] -= 1
    elif playerInput == "s" and maze[playerStats[1]+1][playerStats[0]] == "." or maze[playerStats[1]+1][playerStats[0]] == "E":
        maze[playerStats[1]][playerStats[0]] = "." 
        maze[playerStats[1]+1][playerStats[0]] = "@"
        forest[playerStats[1]][playerStats[0]] = "." 
        forest[playerStats[1]+1][playerStats[0]] = "@"
        playerStats[1] += 1
    elif playerInput == "e" and maze[playerStats[1]][playerStats[0]+1] == "." or maze[playerStats[1]][playerStats[0]+1] == "E":
        maze[playerStats[1]][playerStats[0]] = "." 
        maze[playerStats[1]][playerStats[0]+1] = "@"
        forest[playerStats[1]][playerStats[0]] = "." 
        forest[playerStats[1]][playerStats[0]+1] = "@"
        playerStats[0] += 1
    elif playerInput == "w" and maze[playerStats[1]][playerStats[0]-1] == "." or maze[playerStats[1]][playerStats[0]-1] == "E":
        maze[playerStats[1]][playerStats[0]] = "." 
        maze[playerStats[1]][playerStats[0]-1] = "@"
        forest[playerStats[1]][playerStats[0]] = "." 
        forest[playerStats[1]][playerStats[0]-1] = "@"
        playerStats[0] -= 1
    else:
        print("ERROR!")
    
    playerEnergy -= 1
    
    return playerStats, playerEnergy, maze, forest

def initGame(mazeWidth, mazeHeight):
    maze = initMaze(mazeWidth, mazeHeight)
    
    playerStats = initGamePiece("@", mazeWidth, mazeHeight, maze)
    exitStats = initGamePiece("E", mazeWidth, mazeHeight, maze)
    forest = createRawMaze(" ", mazeWidth, mazeHeight)
    forest[playerStats[1]][playerStats[0]] = "@"

    return maze, forest, playerStats, exitStats

def setVisibility(radius, playerStats, mazeWidth, mazeHeight, maze, forest):
    rx = radius
    ry = radius

    #   012345678
    #  ---X
    if playerStats[0] + rx > mazeWidth-1:
        rx = mazeWidth - playerStats[0]-1
    elif playerStats[0] - rx < 0:
        rx = playerStats[0]

    if playerStats[1] + ry > mazeHeight-1:
        ry = mazeHeight - playerStats[1]-1
    elif playerStats[1] - ry < 0:
        ry = playerStats[1]

    for i in range(-ry, ry + 1):
        for j in range(-rx, rx + 1):
            if abs(playerStats[0] - (playerStats[0]+j)) + abs(playerStats[1] - (playerStats[1]+i)) <= radius:
                forest[playerStats[1]+i][playerStats[0]+j] = maze[playerStats[1]+i][playerStats[0]+j]
    
    return forest
            
def main():
    colorama.init(autoreset=True)

    gameOver = False

    mazeWidth = 41
    mazeHeight = 13

    INITIAL_ENERGY = (mazeWidth * mazeHeight) // 16
    playerEnergy = INITIAL_ENERGY

    print("Forest Escape!")
    print()

    print("By: Matthew Holman")
    print("[COM S 127]")
    print()

    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, [q]uit?: ")
        while choice != "p" and choice != "i" and choice != "q":
                print("ERROR - Please Enter p, i, or q...")
                choice = input("MAIN MENU: [p]lay, [i]nstructions, [q]uit?: ")
        if choice == "p":
            quitEarly = False
            maze, forest, playerStats, exitStats = initGame(mazeWidth, mazeHeight)

            while playerStats != exitStats:
                forest = setVisibility(3, playerStats, mazeWidth, mazeHeight, maze, forest)
                #renderMaze(maze)
                renderMaze(forest)

                print("You have {0} energy remaining.".format(playerEnergy))
                playerInput = input("MOVEMENT: [n], [s], [e], [w], [q]uit?: ")
                while playerInput != "n" and playerInput != "s" and playerInput != "e" and playerInput != "w" and playerInput != "q":
                    print("ERROR - Please Enter n, s, e, w, or q...")
                    playerInput = input("MOVEMENT: [n], [s], [e], [w]?: ")
                if playerInput == "q":
                    quitEarly = True
                    break
                playerStats, playerEnergy, maze, forest = playerMovement(playerInput, playerStats, playerEnergy, maze, forest)
                if playerEnergy <= 0:
                    break
            if quitEarly == False and playerEnergy > 0:
                renderMaze(maze)
                print("You have ESCAPED from the forest! You had {0} energy left when you made it out!".format(playerEnergy))
                print()
            elif quitEarly == False and playerEnergy <= 0:
                renderMaze(maze)
                print("You have GOTTEN LOST in the forest! You had {0} energy and couldn't make it!".format(playerEnergy))
                print()
            else:
                quitEarly = False
            playerEnergy = INITIAL_ENERGY
        elif choice == "i":
            print("Navigate the forest to find the exit (E)!")
            print()
        elif choice == "q":
            gameOver = True
            print("Goodbye!")
            print()

if __name__ == "__main__":
    main()