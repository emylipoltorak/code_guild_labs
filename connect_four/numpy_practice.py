import numpy as np

board = np.full((6, 7), '')


def drop_token(token, col):
    for x in reversed(range(6)):
        if board[x, col-1] == '':
            row = x
            board[row, col - 1] = token
            break


if __name__ == '__main__':
    print(board)
