# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the
# very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

numbers_of_guesses = 0
win_number = random.randint(1, 9)
while True:
    guess = input("Guess the number: ")

    if guess == "exit":
        exit()
    elif guess == str(win_number):
        print("You Win!!")
        break

    else:
        numbers_of_guesses += 1
        print("Numbers of guesses = " + str(numbers_of_guesses))
