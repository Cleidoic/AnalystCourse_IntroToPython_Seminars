import main


def draw_board():
    print('-' * 20)
    for i in range(3):
        for k in range(3):
            print(f"{main.board[k + i * 3]:^5}", end=" ")
        print(f"\n{'-' * 20}")
    print()
