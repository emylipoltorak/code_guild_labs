import numpy as np

board = np.zeros((7, 7), str)


def drop_token(token, x):
    board[-1,x-1] = token


if __name__ == '__main__':
    print(board)
    drop_token('Y',4)
    print('')
    print('***')
    print('')
    print(board)
