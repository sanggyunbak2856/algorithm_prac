import sys

n = int(sys.stdin.readline())
board = [[' ']*n for __ in range(n)]

def draw(n, col, row):
    if n == 3:
        board[col][row] = '*'
        board[col][row + 1] = '*'
        board[col][row + 2] = '*'
        board[col + 1][row] = '*'
        board[col + 1][row + 2] = '*'
        board[col + 2][row] = '*'
        board[col + 2][row + 1] = '*'
        board[col + 2][row + 2] = '*'
    else:
        draw(n // 3, col, row)
        draw(n // 3, col, row + n // 3)
        draw(n // 3, col, row + 2 * n // 3)
        draw(n // 3, col + n // 3, row)
        draw(n // 3, col + n // 3, row + 2 * n // 3)
        draw(n // 3, col + 2 * n // 3, row)
        draw(n // 3, col + 2 * n // 3, row + n // 3)
        draw(n // 3, col + 2 * n // 3, row + 2 * n // 3)

def printBoard(board):
    for col in board:
        print(''.join(col))

draw(n, 0, 0)
printBoard(board)

