from token import Token


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = self.build_board()

    def build_board(self):
        self.board = [[] for x in range(self.rows)]
        for row in self.board:
            for x in range(self.cols):
                row.append(Token(row, x))
        return self.board

    def drop_token(self, col, token):
        for row in reversed(range(self.rows)):
            if not self.board[row][col-1].color:
                self.board[row][col-1].color = token
                return self.board

    def __str__(self):
        return '\n'.join(str(', '.join(str(x) for x in self.board[self.board.index(row)]))for row in self.board)


if __name__ == '__main__':
    b = Board(7, 6)
    # print(b)
    b.drop_token(2, 'Y')
    b.drop_token(2, 'Y')
    b.drop_token(2, 'R')
    print(b)
