import main


def place_sign(token):
    main.board
    while True:
        answer = input(f"Enter a number from 1 to 9.\nSelect a position {token}? ")
        if answer.isdigit() and int(answer) in range(1, 10):
            answer = int(answer)
            pos = main.board[answer - 1]
            if pos not in (chr(10060), chr(11093)):
                main.board[answer - 1] = chr(10060) if token == "X" else chr(11093)
                break
            else:
                print(f"This cell is already occupied{chr(9995)}{chr(129292)}")
        else:
            print(f"Incorrect input{chr(9940)}, Are you sure you entered a correct number?")
