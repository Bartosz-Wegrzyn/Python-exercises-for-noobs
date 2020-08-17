#  This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.
#
# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to
# guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the
# actual game, the player can only guess 6 letters incorrectly before losing).
#
# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to
# guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an
# infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed
# and display a different message if the player tries to guess that letter again. Remember to stop the game when all
# the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number
# of guesses the player has remaining - we will deal with those in a future exercise.
#
# An example interaction can look like this:
#
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on, until the player gets the word.


from Task_30 import random_word

print("Welcome to Hangman!")

def Game(word):
    number_of_guesses_left = 6
    letters_guesses = ""

    print(Print_word(word, "Ü"))

    while number_of_guesses_left > 0:

        while True:
            guess = input("Guess your letter: ").upper()
            if guess in letters_guesses:
                print(f"You arledy checkd {guess}")
            else:
                break


        if guess in word:
            letters_guesses += guess
            print(Print_word(word, letters_guesses))
            if "_" in Print_word(word, letters_guesses):
                pass
            else:
                print("You Win!")
                exit()

        else:
            print("incorrect")
            number_of_guesses_left -= 1

    else:
        print("you lose")
        print("Correct word: ", end="")
        print(word)


def Print_word(word, letters_guesses):
        string_to_return = ""
        for letters in word:

            if letters in letters_guesses:
                string_to_return += " " + letters + " "
            else:
                string_to_return += " _ "
        return string_to_return





Game(random_word().upper())











