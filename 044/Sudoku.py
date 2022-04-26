# -*- coding: utf-8 -*-

class Sudoku():
    def sudoku(self, board: 'list[int]') -> 'bool':
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for k in range(1, 10):
                        board[i][j] = k
                        print(self.check(board, i, j))
                        self.showBoard(board)
                        if self.check(board, i, j) and self.sudoku(board):
                            return True
                        ## with this k, it doesn't work out
                        ## reset the tile to 0, in case 9 doesn't work out here
                        board[i][j] = 0
                    ## 1 to 9 all don't work out for this tile
                    return False
        ## when recursing, and there is no zero in the board, return True
        return True
    
    def check(self, board: 'list[list[int]]', x: 'int', y: 'int') -> 'bool':
        for i in range(9):
            ## check column
            if i != x and board[i][y] == board[x][y]: return False
            ## check row
            if i != y and board[x][i] == board[x][y]: return False
        ## check square
        m, n = 3 * (x // 3), 3 * (y // 3) ## the m, n th 3 * 3 square
        for i in range(3):
            for j in range(3):
                if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                    return False
        return True
    def showBoard(self, board):
        for i in range(9):
            print(board[i])
        print()

def main():
    test = Sudoku()
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
    if test.sudoku(board):
        for i in board:
            print(' '.join(list(map(str, i))))
    # for i in range(1, 10):
    #     board[0][0] = i
    #     print(f"{i}, {test.check(board, 0, 0)}")

if __name__ == "__main__":
    main()