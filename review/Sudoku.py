# -*- coding: utf-8 -*-

def sudoku(board: "list[list[int]]") -> "bool":
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in "123456789":
                    board[i][j] = int(k)
                    if check(board, i, j) and sudoku(board):
                        return True
                    board[i][j] = 0
                return False
    return True

def check(board: "list[list[int]]", x: "int", y: "int") -> "bool":
    ## check row and column
    for i in range(9):
        if board[i][y] == board[x][y] and i != x: return False
        if board[x][i] == board[x][y] and i != y: return False
    ## check square
    m, n = x // 3, y // 3
    for i in range(3):
        for j in range(3):
            if board[x][y] == board[3 * m + i][3 * n + j] and (x != 3 * m + i or y != 3 * n + j): return False
    return True

def transform_test_case(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                board[i][j] = 0
            else:
                board[i][j] = int(board[i][j])
    return board

def main():
    board = [
        [0, 9, 2, 4, 8, 1, 7, 6, 3],
        [4, 1, 3, 7, 6, 2, 9, 8, 5],
        [8, 6, 7, 3, 5, 9, 4, 1, 2],
        [6, 2, 4, 1, 9, 5, 3, 7, 8],
        [7, 5, 9, 8, 4, 3, 1, 2, 0],
        [1, 3, 8, 6, 2, 7, 5, 9, 4],
        [2, 7, 1, 5, 3, 8, 6, 4, 9],
        [3, 8, 6, 9, 1, 4, 2, 5, 7],
        [0, 4, 5, 2, 7, 6, 8, 3, 1]
    ]
    board2 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    # for line in board2:
    #     print(line)
    board2 = transform_test_case(board2)
    # for line in board2:
    #     print(line)
    # sudoku(board)
    sudoku(board2)
    # for line in board:
    #     print(line)
    for line in board2:
        print(line)

if __name__ == "__main__":
    main()
