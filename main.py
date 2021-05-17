"""
◘◘◘◘◘◘◘◘◘◘◘◘◘
◘◘◘ Notes ◘◘◘
◘◘◘◘◘◘◘◘◘◘◘◘◘
#########################
### Example maze maps ###
#########################
MAZE_FILENAME = "maze2x2.txt" 
MAZE_FILENAME = "maze3x3.txt"
MAZE_FILENAME = "maze5x5.txt"
MAZE_FILENAME = "maze10x10.txt"
MAZE_FILENAME = "maze15x20.txt" # Warning! This could take serveral time to analyze.
"""

from simpleimage import SimpleImage
import codecs
import sys

MAZE_FILENAME = "maze10x10.txt"

# ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘

# ◘◘◘◘◘◘◘◘◘◘◘◘
# ◘◘◘ Main ◘◘◘
# ◘◘◘◘◘◘◘◘◘◘◘◘
def main():
    print("◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥♥♥ Start ♥♥♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥")
    maze = readMazeFromFile(MAZE_FILENAME)
    mazeWidth = len(maze[0])
    mazeHeight = len(maze)
    print("mazeWidth:", mazeWidth)
    print("mazeheight:", mazeHeight)
    for column in range(mazeHeight):
        for row in range(mazeWidth):
            if maze[column][row] == "A":
                startPos = {"x": row, "y": column}
    for column in range(mazeHeight):
        for row in range(mazeWidth):
            if maze[column][row] == "Z":
                endPos = {"x": row, "y": column}
    print("startPos:", startPos)
    print("endPos:", endPos)
    mazeInitialData = {"maze": maze, "mazeWidth": mazeWidth, "mazeHeight": mazeHeight, "startPos": startPos, "endPos": endPos}
    printInitialMaze(mazeInitialData)
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥♥♥ Process ♥♥♥")
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    ##################
    ### Path ~ m=1 ###
    ##################
    movements = 1
    entirePath = []
    actualPosX = startPos["x"]
    actualPosY = startPos["y"]
    # ============================================================================================
    directionToGo = "↑"
    resultOfGo, (positionToGoX, positionToGoY) = getNeighborBox(maze, actualPosX, actualPosY, directionToGo)
    if resultOfGo == "validMove" or resultOfGo == "end":
        entirePath.append(directionToGo)
        checkEnd(resultOfGo, entirePath, mazeInitialData)
    directionToGo = "→"
    resultOfGo, (positionToGoX, positionToGoY) = getNeighborBox(maze, actualPosX, actualPosY, directionToGo)
    if resultOfGo == "validMove" or resultOfGo == "end":
        entirePath.append(directionToGo)
        checkEnd(resultOfGo, entirePath, mazeInitialData)
    directionToGo = "↓"
    resultOfGo, (positionToGoX, positionToGoY) = getNeighborBox(maze, actualPosX, actualPosY, directionToGo)
    if resultOfGo == "validMove" or resultOfGo == "end":
        entirePath.append(directionToGo)
        checkEnd(resultOfGo, entirePath, mazeInitialData)
    directionToGo = "←"
    resultOfGo, (positionToGoX, positionToGoY) = getNeighborBox(maze, actualPosX, actualPosY, directionToGo)
    if resultOfGo == "validMove" or resultOfGo == "end":
        entirePath.append(directionToGo)
        checkEnd(resultOfGo, entirePath, mazeInitialData)
    print("m=" + str(movements) + ":", str(len(entirePath)) + " analizablyPaths", entirePath)
    ##################
    ### Path ~ m>1 ###
    ##################
    while True:
        movements += 1
        subPaths = []
        # ============================
        for currentPath in entirePath:
            lastPositions = getLastPositions(startPos, currentPath)
            actualPos = getActualPos(startPos, currentPath)
            actualPosX = actualPos["x"]
            actualPosY = actualPos["y"]
            # ======================================================================================================
            directionToGo = "↑"
            resultOfGo, (positionToGoX, positionToGoY) = getNeighborBox(maze, actualPosX, actualPosY, directionToGo)
            if resultOfGo == "validMove" or resultOfGo == "end":
                if [positionToGoX, positionToGoY] not in lastPositions:
                    currentExtension = generateExtension(currentPath, directionToGo)
                    subPaths.append(currentExtension)
                    checkEnd(resultOfGo, currentExtension, mazeInitialData)
            directionToGo = "→"
            resultOfGo, (positionToGoX, positionToGoY) = getNeighborBox(maze, actualPosX, actualPosY, directionToGo)
            if resultOfGo == "validMove" or resultOfGo == "end":
                if [positionToGoX, positionToGoY] not in lastPositions:
                    currentExtension = generateExtension(currentPath, directionToGo)
                    subPaths.append(currentExtension)
                    checkEnd(resultOfGo, currentExtension, mazeInitialData)
            directionToGo = "↓"
            resultOfGo, (positionToGoX, positionToGoY) = getNeighborBox(maze, actualPosX, actualPosY, directionToGo)
            if resultOfGo == "validMove" or resultOfGo == "end":
                if [positionToGoX, positionToGoY] not in lastPositions:
                    currentExtension = generateExtension(currentPath, directionToGo)
                    subPaths.append(currentExtension)
                    checkEnd(resultOfGo, currentExtension, mazeInitialData)
            directionToGo = "←"
            resultOfGo, (positionToGoX, positionToGoY) = getNeighborBox(maze, actualPosX, actualPosY, directionToGo)
            if resultOfGo == "validMove" or resultOfGo == "end":
                if [positionToGoX, positionToGoY] not in lastPositions:
                    currentExtension = generateExtension(currentPath, directionToGo)
                    subPaths.append(currentExtension)
                    checkEnd(resultOfGo, currentExtension, mazeInitialData)
        entirePath = subPaths
        if len(entirePath) <= 10:
            print("m=" + str(movements) + ":", str(len(entirePath)) + " analizablyPaths", entirePath)
        else:
            print("m=" + str(movements) + ":", str(len(entirePath)) + " analizablyPaths", "[...]")


# ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘

# ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘
# ◘◘◘ Functions ◘◘◘
# ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘


def readMazeFromFile(fileName):
    with codecs.open(fileName, "r", "utf-8") as f:
        mazeTXT = f.read().replace(" ", "").replace("\n", "").replace("\r", "-")
    row = []
    maze = []
    for index, letter in enumerate(range(len(mazeTXT))):
        if mazeTXT[letter] != "-":
            row.append(mazeTXT[letter])
        if mazeTXT[letter] == "-" or index == len(mazeTXT) - 1:
            maze.append(row)
            row = []
    return maze


def getNeighborBox(maze, posX, posY, direction):
    toPosX, toPosY = getPositionToGo(posX, posY, direction)
    if isMoveValidTo(maze, toPosX, toPosY):
        if maze[toPosY][toPosX] == "Z":
            neighborBox = "end"
        else:
            neighborBox = "validMove"
    elif not isMoveValidTo(maze, toPosX, toPosY):
        neighborBox = "invalidMove"
    return neighborBox, [toPosX, toPosY]


def isMoveValidTo(maze, toPosX, toPosY):
    mazeWidth = len(maze[0])
    mazeHeight = len(maze)
    return toPosX >= 0 and toPosX <= mazeWidth - 1 and toPosY >= 0 and toPosY <= mazeHeight - 1 and maze[toPosY][toPosX] != "#"


def getPositionToGo(posX, posY, direction):
    if direction == "↑":
        toPosX = posX + 0
        toPosY = posY - 1
    elif direction == "→":
        toPosX = posX + 1
        toPosY = posY + 0
    elif direction == "↓":
        toPosX = posX + 0
        toPosY = posY + 1
    elif direction == "←":
        toPosX = posX - 1
        toPosY = posY + 0
    return [toPosX, toPosY]


def getLastPositions(startPos, path):
    currentPosX = startPos["x"]
    currentPosY = startPos["y"]
    lastPositions = [[startPos["x"], startPos["y"]]]
    for direction in path:
        if direction == "↑":
            currentPosX += 0
            currentPosY -= 1
            lastPositions.append([currentPosX, currentPosY])
        elif direction == "→":
            currentPosX += 1
            currentPosY += 0
            lastPositions.append([currentPosX, currentPosY])
        elif direction == "↓":
            currentPosX += 0
            currentPosY += 1
            lastPositions.append([currentPosX, currentPosY])
        elif direction == "←":
            currentPosX -= 1
            currentPosY += 0
            lastPositions.append([currentPosX, currentPosY])
    return lastPositions


def getActualPos(startPos, path):
    currentPosX = startPos["x"]
    currentPosY = startPos["y"]
    for direction in path:
        if direction == "↑":
            currentPosX += 0
            currentPosY -= 1
        elif direction == "→":
            currentPosX += 1
            currentPosY += 0
        elif direction == "↓":
            currentPosX += 0
            currentPosY += 1
        elif direction == "←":
            currentPosX -= 1
            currentPosY += 0
    return {"x": currentPosX, "y": currentPosY}


def generateExtension(path, direction):
    newPath = []
    for i in path:
        newPath.append(i)
    newPath.append(direction)
    return newPath


def checkEnd(directionToGo, shortestPath, mazeInitialData):
    if directionToGo == "end":
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("♥♥♥♥♥♥♥♥♥♥♥")
        print("♥♥♥ End ♥♥♥")
        print("♥♥♥♥♥♥♥♥♥♥♥")
        print("shortestPath:", shortestPath)
        print("numberOfMovements:", len(shortestPath))
        printMazeShortestPath(mazeInitialData, shortestPath)
        print("◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")
        sys.exit()


def printMazeShortestPath(mazeInitialData, path):
    print("::::::::::::")
    print("::: Draw :::")
    print("::::::::::::")
    maze = mazeInitialData["maze"]
    mazeWidth = mazeInitialData["mazeWidth"]
    mazeHeight = mazeInitialData["mazeHeight"]
    startPos = mazeInitialData["startPos"]
    lastPositions = getLastPositions(startPos, path)
    # --------------------------------------------------
    for index, (posX, posY) in enumerate(lastPositions):
        if maze[posY][posX] != "A" and maze[posY][posX] != "Z" and maze[posY][posX] != "#":
            maze[posY][posX] = path[index]
    for column in range(mazeHeight):
        for row in range(mazeWidth):
            box = "○" if (maze[column][row] == " " or maze[column][row] == "○") else maze[column][row]
            box = " " + box + " "
            print(box[1:], end="") if row == 0 else print(box, end="")
        print()
    generateShortestPathImage(mazeInitialData)


def generateShortestPathImage(mazeInitialData):
    IMAGE_SIZE_IN_PIXELS = 20
    maze = mazeInitialData["maze"]
    mazeWidth = mazeInitialData["mazeWidth"]
    mazeHeight = mazeInitialData["mazeHeight"]
    blankWidth = mazeWidth * IMAGE_SIZE_IN_PIXELS
    blankHeight = mazeHeight * IMAGE_SIZE_IN_PIXELS
    blank = SimpleImage.blank(blankWidth, blankHeight)
    a = SimpleImage('a.png')
    z = SimpleImage('z.png')
    wall = SimpleImage('wall.png')
    free = SimpleImage('free.png')
    upArrow = SimpleImage('upArrow.png')
    rightArrow = SimpleImage('rightArrow.png')
    downArrow = SimpleImage('downArrow.png')
    leftArrow = SimpleImage('leftArrow.png')
    # ----------------------------------------------------------------
    aList = []
    zList = []
    wallList = []
    freeList = []
    upArrowList = []
    rightArrowList = []
    downArrowList = []
    leftArrowList = []
    for column in range(mazeHeight):
        for row in range(mazeWidth):
            if maze[column][row] == "A":
                aList.append([column, row])
            elif maze[column][row] == "Z":
                zList.append([column, row])
            elif maze[column][row] == "#":
                wallList.append([column, row])
            elif maze[column][row] == " " or maze[column][row] == "○":
                freeList.append([column, row])
            elif maze[column][row] == "↑":
                upArrowList.append([column, row])
            elif maze[column][row] == "→":
                rightArrowList.append([column, row])
            elif maze[column][row] == "↓":
                downArrowList.append([column, row])
            elif maze[column][row] == "←":
                leftArrowList.append([column, row])
    # ----------------
    # --- Insert A ---
    # ----------------
    actualImage = a
    for posYToInsert, posXToInsert in aList:
        for y in range(actualImage.width):
            for x in range(actualImage.height):
                pixel = actualImage.get_pixel(x, y)
                blank.set_pixel(x + (posXToInsert * blankWidth / mazeWidth), y + (posYToInsert * blankHeight / mazeHeight), pixel)
    # -----------------
    # --- Insert Z ---
    # -----------------
    actualImage = z
    for posYToInsert, posXToInsert in zList:
        for y in range(actualImage.width):
            for x in range(actualImage.height):
                pixel = actualImage.get_pixel(x, y)
                blank.set_pixel(x + (posXToInsert * blankWidth / mazeWidth), y + (posYToInsert * blankHeight / mazeHeight), pixel)
    # ---------------------
    # --- Insert wall/s ---
    # ---------------------
    actualImage = wall
    for posYToInsert, posXToInsert in wallList:
        for y in range(actualImage.width):
            for x in range(actualImage.height):
                pixel = actualImage.get_pixel(x, y)
                blank.set_pixel(x + (posXToInsert * blankWidth / mazeWidth), y + (posYToInsert * blankHeight / mazeHeight), pixel)
    # ---------------------
    # --- Insert free/s ---
    # ---------------------
    actualImage = free
    for posYToInsert, posXToInsert in freeList:
        for y in range(actualImage.width):
            for x in range(actualImage.height):
                pixel = actualImage.get_pixel(x, y)
                blank.set_pixel(x + (posXToInsert * blankWidth / mazeWidth), y + (posYToInsert * blankHeight / mazeHeight), pixel)
    # ------------------------
    # --- Insert upArrow/s ---
    # ------------------------
    actualImage = upArrow
    for posYToInsert, posXToInsert in upArrowList:
        for y in range(actualImage.width):
            for x in range(actualImage.height):
                pixel = actualImage.get_pixel(x, y)
                blank.set_pixel(x + (posXToInsert * blankWidth / mazeWidth), y + (posYToInsert * blankHeight / mazeHeight), pixel)
    # ---------------------------
    # --- Insert rightArrow/s ---
    # ---------------------------
    actualImage = rightArrow
    for posYToInsert, posXToInsert in rightArrowList:
        for y in range(actualImage.width):
            for x in range(actualImage.height):
                pixel = actualImage.get_pixel(x, y)
                blank.set_pixel(x + (posXToInsert * blankWidth / mazeWidth), y + (posYToInsert * blankHeight / mazeHeight), pixel)
    # --------------------------
    # --- Insert downArrow/s ---
    # --------------------------
    actualImage = downArrow
    for posYToInsert, posXToInsert in downArrowList:
        for y in range(actualImage.width):
            for x in range(actualImage.height):
                pixel = actualImage.get_pixel(x, y)
                blank.set_pixel(x + (posXToInsert * blankWidth / mazeWidth), y + (posYToInsert * blankHeight / mazeHeight), pixel)
    # --------------------------
    # --- Insert leftArrow/s ---
    # --------------------------
    actualImage = leftArrow
    for posYToInsert, posXToInsert in leftArrowList:
        for y in range(actualImage.width):
            for x in range(actualImage.height):
                pixel = actualImage.get_pixel(x, y)
                blank.set_pixel(x + (posXToInsert * blankWidth / mazeWidth), y + (posYToInsert * blankHeight / mazeHeight), pixel)
    blank.show()


def printInitialMaze(mazeInitialData):
    print("::::::::::::")
    print("::: Draw :::")
    print("::::::::::::")
    maze = mazeInitialData["maze"]
    mazeWidth = mazeInitialData["mazeWidth"]
    mazeHeight = mazeInitialData["mazeHeight"]
    for column in range(mazeHeight):
        for row in range(mazeWidth):
            box = "○" if (maze[column][row] == " " or maze[column][row] == "○") else maze[column][row]
            box = " " + box + " "
            print(box[1:], end="") if row == 0 else print(box, end="")
        print()


# ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘

if __name__ == "__main__":
    main()
