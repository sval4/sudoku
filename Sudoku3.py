import lab06_util

def check_col(col, bd, num):
    list = []
    for i in range(len(bd)):
        list.append(bd[i][col])
    return list.count(str(num)) == 0

def check_block(row, col, bd, num):
    if row % 3 == 0:
        rows = (row, row + 1, row + 2)
    elif row % 3 == 1:
        rows = (row - 1, row, row + 1)
    elif row % 3 == 2:
        rows = (row - 2, row - 1, row)
        
    if col % 3 == 0:
        cols = (col, col + 1, col + 2)
    elif col % 3 == 1:
        cols = (col - 1, col, col + 1)
    elif col % 3 == 2:
        cols = (col - 2, col - 1, col)
    
    for i in rows:
        for j in cols:
            if bd[i][j] == str(num):
                return False
    return True
        

def ok_to_add(row, col, bd, num):
    temp = bd[row][col]
    bd[row][col] = "."
    if row < 0 or row >= len(bd) or col < 0 or col >= len(bd[0]) or num < 1 or num > 9:
        bd[row][col] = temp
        return False
    elif bd[row][col] != ".":
        bd[row][col] = temp
        return False
    elif bd[row].count(str(num)) != 0:
        bd[row][col] = temp
        return False
    elif not(check_col(col, bd, num)):
        bd[row][col] = temp
        return False
    elif not(check_block(row, col, bd, num)):
        bd[row][col] = temp
        return False
    bd[row][col] = temp
    return True
    
    
def print_board(bd):
    horizontal_counter = 3
    vertical_counter = 3
    check1 = False
    check2 = False
    for i in range(len(bd)):
        if horizontal_counter == 3:
            horizontal_counter = 0
            if i == 0:
                print("-" * (2 * (len(bd[0]) + (len(bd[0]) // 3)) + 1), end = "")
            else:
                print()
                print("-" * (2 * (len(bd[0]) + (len(bd[0]) // 3)) + 1), end = "")
            check1 = True
        print()
        for j in range(len(bd[i])):
            if vertical_counter == 3:
                check2 = True
                vertical_counter = 0
                if j == 0:
                    print("|", end = "")
                else:
                    print(" |", end = "")
            print(" " + bd[i][j], end = "")
            if j == len(bd[i]) - 1:
                print(" |", end = "")
            if check2:
                check2 = False
                j -= 1
            vertical_counter += 1
        if check1:
            check1 = False
            i -= 1
        horizontal_counter += 1
    print()
    print("-" * (2 * (len(bd[0]) + (len(bd[0]) // 3)) + 1), end = "")
    
def solution_verifier(board):
    for i in range(len(board)):
        if board[i].count(".") != 0:
            return False
        for j in range(len(board[i])):
            temp = board[i][j]
            board[i][j] = "."
            if not(ok_to_add(i, j, board, int(temp))):
                return False
            board[i][j] = temp
    return True
                
    
board = input("Enter the file: ")
board = board.strip()
board = lab06_util.read_sudoku(board)
print_board(board)


while not(solution_verifier(board)):
    row = input("Enter a row: ")
    row = int(row)
    
    col = input("Enter a column: ")
    col = int(col)
    
    num = input("Enter a number: ")
    num = int(num)
    
    if ok_to_add(row, col, board, num):
        board[row][col] = str(num)
    print_board(board)