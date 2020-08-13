# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
# message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

rock = ["Rock", "R", "r"]
paper = ["paper", "Paper", "p", "P"]
scissors = ["Scissors", "scissors", "S", "s"]


def Rock_Paper_Scissors_is_1P_win(First_player_choice, second_player_choice):
    if First_player_choice in rock:
        First_player_choice = rock
    elif First_player_choice in paper:
        First_player_choice = paper
    elif First_player_choice in scissors:
        First_player_choice = scissors
    else:
        print("Wrong choice")
        exit()

    if second_player_choice in rock:
        second_player_choice = rock
    elif second_player_choice in paper:
        second_player_choice = paper
    elif second_player_choice in scissors:
        second_player_choice = scissors
    else:
        print("Wrong choice")
        exit()

    if First_player_choice == second_player_choice:
        return None
    if First_player_choice == paper and second_player_choice == rock:
        return True
    if First_player_choice == scissors and second_player_choice == paper:
        return True
    if First_player_choice == rock and second_player_choice == scissors:
        return True
    if First_player_choice == rock and second_player_choice == paper:
        return False
    if First_player_choice == paper and second_player_choice == scissors:
        return False
    if First_player_choice == scissors and second_player_choice == rock:
        return False


while True:
    firstPlayer = str(input("Rock, Paper, Scissors?: "))
    secondPlayer = str(input("Rock, Paper, Scissors?: "))

    game = Rock_Paper_Scissors_is_1P_win(firstPlayer, secondPlayer)

    if game == None:
        print("draw")
    elif game:
        print("1 Player Win")
    elif not game:
        print("2 Player Win")
