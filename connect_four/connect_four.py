from game_board import Board


def connect_four(file):
    with open(file, 'r') as f:
        moves = [int(line.strip()) for line in f.readlines()]
    b = Board(6, 7)
    for move in moves:
        if not moves.index(move) % 2:
            b.drop_token(move, 'Y')
            print(b)
            print('')
        else:
            b.drop_token(move, 'R')
            print(b)
            print('')
    return b


if __name__ == '__main__':
    connect_four('moves.txt')
