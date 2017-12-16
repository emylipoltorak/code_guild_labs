import numpy as np
from game_piece import Token


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.full((rows, cols), '')

    def build_board(self):
        for row in self.rows:
            for col in self.cols:
                self.board[row,col]


    def drop_piece(self, col, color):
        for x in reversed(range(self.rows)):
            if self.board[x, col - 1] == '':
                row = x
                self.board[row, col - 1] = color
                break

