You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.  
Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.


def path_finder(maze):
    maze = maze.split()
    matrix =[ list(i) for i in maze]
    floodFill(matrix,0,0,".","*")
    return True if matrix[-1][-1] =="*" else False

def floodFill(world, x, y, oldChar, newChar):
    worldWidth = len(world)
    worldHeight = len(world)
    if world[x][y] != oldChar:
        return
    world[x][y] = newChar
    try:
        if x > 0: # left
            floodFill(world, x-1, y, oldChar, newChar)
        if y > 0: # up
            floodFill(world, x, y-1, oldChar, newChar)
        if x < worldWidth-1: # right
            floodFill(world, x+1, y, oldChar, newChar)
        if y < worldHeight-1: # down
            floodFill(world, x, y+1, oldChar, newChar)
        
