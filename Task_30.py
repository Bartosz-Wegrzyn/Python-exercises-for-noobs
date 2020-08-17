# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.
#
# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS
# dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s
# compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a
# single word.
#
# Hint: use the Python random library for picking a random word.
import random


def random_word():
    swopods = {}
    i = 0
    with open('scr/sowpods.txt',) as l:
        line = l.readline()
        while line:

            swopods[i] = line
            i += 1
            line = l.readline()

    r = random.randint(0,len(swopods))
    return swopods[r]