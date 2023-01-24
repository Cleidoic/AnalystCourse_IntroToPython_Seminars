import main


def c_w():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [main.board[x[0]] for x in win_coord if main.board[x[0]] == main.board[x[1]] == main.board[x[2]]]
    return n[0] if n else n
