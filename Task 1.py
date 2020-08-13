# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Hi! What is your name?: ")

try:
    age = int(input("And what is your age?: "))
except ValueError:
    print( "Valie Error")
    exit()

when = 2020 - age + 100


print(name + " You will be 100 years old in " + str(when))