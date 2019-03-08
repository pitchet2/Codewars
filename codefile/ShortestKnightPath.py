board = [['a8','b8','c8','d8','e8','f8','g8','h8'],
         ['a7','b7','c7','d7','e7','f7','g7','h7'],
         ['a6','b6','c6','d6','e6','f6','g6','h6'],
         ['a5','b5','c5','d5','e5','f5','g5','h5'],
         ['a4','b4','c4','d4','e4','f4','g4','h4'],
         ['a3','b3','c3','d3','e3','f3','g3','h3'],
         ['a2','b2','c2','d2','e2','f2','g2','h2'],
         ['a1','b1','c1','d1','e1','f1','g1','h1'],]

def knight(p1, p2):
    bag = set()
    end = ()
    counter = 0
    for y,row in enumerate(board):
        for x,ele in enumerate(row):
            if ele == p1:
                bag.add((y,x))
            if ele == p2:
                end = (y,x)
    while end not in bag:
        for i in bag:
            y = i[0]
            x = i[1]
            new_coor = list(get_neighbours(board,y,x))
            new_bag = list(bag) + new_coor
            bag = set(new_bag)
        counter +=1
    return counter

def get_neighbours(matrix,y, x):
    directions = {(-2,-1),(-2,1),(-1,-2),(-1,2),(2,-1),(2,1),(1,-2),(1,2)}
    neighbours = set()
    for dy, dx in directions:
        if 0 <= y + dy < len(matrix) and 0 <= x + dx < len(matrix):
            neighbours.add((y+dy,x+dx))
    return neighbours

