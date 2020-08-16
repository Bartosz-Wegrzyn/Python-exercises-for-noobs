def make_full_row(board_size):
    row = " ---"
    r = ""
    for times in range(board_size):
        r += row
    return r


def make_full_colum(board_size, x_or_o, col):
    c = ""

    if x_or_o == 1:
        x_or_o = "x"
    elif x_or_o == 2:
        x_or_o = "o"
    else:
        x_or_o = " "

    for column in range(board_size):
            if column == col:
                c += f"| {x_or_o} "
            else:
                c += f"|   "

    c += "|"
    return c


def meke_fill_board(board_size, x_or_o, col, row):
    for times in range(board_size):
        print(make_full_row(board_size))

        if times == row:
            print(make_full_colum(board_size, x_or_o, col))
        else:
            print(make_full_colum(board_size, 3, board_size+10 ))

    print(make_full_row(board_size))



def who_won_tic_tac_toe(board, size):  # only for 3x3 game


    for i in range(size):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]
    for j in range(size):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j]:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][0]
    return 0


game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("enter coordinates in the form “row, col” - a number, then a comma, then a number:")

game_finish = False

i = 0
while not game_finish:
    if i % 2 == 0:
        round = 1
        i += 1
    else:
        round = 2
        i += 1

    while True:
        choice = input(f"Player's {round} round: ")

        col = int(choice[0]) - 1  # -1 to count from 1 instead 0
        row = int(choice[2]) - 1

        if game[col][row] == 0:
            game[col][row] = round
            meke_fill_board(3, round, int(choice[2])-1, int(choice[0])-1)

            if who_won_tic_tac_toe(game,3):
                print(f"Brawo! Player {who_won_tic_tac_toe(game,3)} win!")
                exit()
            break
        else:
            print("Illegal move")
            continue

    if any(0 in sublist for sublist in game):
        pass
    else:
        print("game is done")
        game_finish = True
