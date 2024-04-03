# Andrew Butler             10-17-2022
# maze demo

# creating grid of maze given width and height
def createRawMaze(mazeWidth, mazeHeight):
    maze = []
    for i in range(0, mazeHeight):
        maze.append([])
        for j in range (0, mazeWidth):
            maze[i].append("#")
    return maze

def renderMaze(maze):
    for row in maze:
        for item in row:
            print(item, end= "")
        print("")


# black magic fuckery
def genMaze(x, y, mazeWidth, mazeHeight, maze):
    # Citation wikipedia (recursive backtracking maze algorithm- iterative version)
    stack = []
    currentCell = None

    # CHoose starting cell and mark it as 'visited'
    maze[y][x] = "."

    # push the newly marked cell to the stack
    stack.append((x, y))

    # run while the stack is not empty
    while len(stack > 0):
        # pop the topmost cell off the stack and assign it to be the currentcell
        currentcell = stack.pop()

        # check for unmarked neighbors (lost me here)
        if ((currentCell[1] + 2 < mazeHeight and maze[currentCell[1]+1][currentCell][0]=="#") or
        (currentCell[1] - 2 < mazeHeight and maze[currentCell[1]+1][currentCell][0]=="#")):





def main():
    mazeWidth = 9
    mazeHeight = 9
    maze = createRawMaze(mazeWidth, mazeHeight)
    renderMaze(maze)
    genMaze(1, 1, mazeWidth, mazeHeight, maze)



if __name__ == "__main__":
    main()