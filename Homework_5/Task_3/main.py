import check_win
import draw_board
import place_sign

board = list(map(str, range(1, 10)))


def main():
    counter = 0
    draw_board.draw_board()
    while True:
        place_sign.place_sign("0") if counter % 2 else place_sign.place_sign("X")
        draw_board.draw_board()

        if counter > 3:
            if check_win.c_w():
                print(f"{check_win.c_w()} - WIN{chr(127942)}{chr(127881)}!")
                break
        if counter == 8:
            print(f"Draw game {chr(129318)}{chr(129309)}!")
            break
        counter += 1


if __name__ == "__main__":
    main()
