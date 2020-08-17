from PIL import Image

from Task_30 import random_word

print("Welcome to Hangman!")


def Game(word):
    number_of_guesses = 0
    correct_guesses = ""
    bad_guesses = ""

    print(Print_word(word, "Ü"))
    img = Image.open('scr/1.png')
    img.show()

    while number_of_guesses < 10:

        while True:
            guess = input("Guess your letter: ").upper()
            if guess in correct_guesses:
                print(f"You arledy checkd {guess}")
            elif guess in bad_guesses:
                print(f"You arledy checkd {guess}")
            else:
                break

        if guess in word:
            correct_guesses += guess
            print(Print_word(word, correct_guesses))
            if "_" in Print_word(word, correct_guesses):
                pass
            else:
                print("You Win!")
                exit()


        else:
            bad_guesses += guess


            number_of_guesses += 1

            img = Image.open(f"scr/{number_of_guesses}.png")
            img.show()
            print(f"incorrect, number od guesses left: {10 - number_of_guesses}")
            print(Print_word(word, correct_guesses))


    else:
        print("you lose")
        img = Image.open(f"scr/11.png")
        img.show()
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
