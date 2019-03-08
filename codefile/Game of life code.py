Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life. The rules of the game are:

Any live cell with fewer than two live neighbours dies, as if caused by underpopulation. Any live cell with more than three live neighbours dies, as if by overcrowding. Any live cell with two or three live neighbours lives on to the next generation. Any dead cell with exactly three live neighbours becomes a live cell. Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. 
The return value should be a 2d array cropped around all of the living cells. 
(If there are no living cells, then return [[]].)

import copy
import numpy as np

def get_generation(cells, generations):
    gen = 0
    print(cells)
    while gen < generations:
        cells = np.pad(cells, pad_width=((1,1),(1,1)),mode ='constant', constant_values=0)
        temp = copy.deepcopy(cells)
        for y,row in enumerate(cells):
            for x,cell in enumerate(row):
                if cell == 0 and get_neighbours(cells,y,x) == 3:
                    temp[y][x] = 1
                if cell == 1 and get_neighbours(cells,y,x) < 2 or get_neighbours(cells,y,x) > 3:
                    temp[y][x] = 0
        cells = temp
        gen += 1
    return de_pad(cells.tolist(),1) if type(cells) != list else de_pad(cells,1)

def get_neighbours(matrix,y, x):
    directions = {(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    neighbours = []
    for dy, dx in directions:
        if 0 <= y + dy < len(matrix) and 0 <= x + dx < len(matrix[0]):
            neighbours.append(matrix[y + dy][x + dx])
    return neighbours.count(1)

def de_pad(matrix, l=1):
    if l == 5:
        return matrix
    while all(p == 0 for p in matrix[0]):
        matrix.pop(0)
    matrix = np.rot90(matrix)
    new_matrix = matrix.tolist()
    return de_pad(new_matrix,l+1)

