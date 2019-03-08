#Check to see if the sudoku solution is valid.

def validSolution(board):
    column =[[row[i] for row in board] for i in range(9)]
    print(column)
    box = [[board[int((m//3)*3)+i][(m%3)*3+j] for i in range(3) for j in range(3)] for m in range(9)]
    if check_valid(board) and check_valid(column) and check_valid(box):
        return True
    else:
        return False

def check_valid(list):
    for i in list:
        if sum(i) != 45:
            return False
    return True
