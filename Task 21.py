# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some
# different code, use the code from the solution), and instead of printing the results to a screen, write the results
# to a txt file. In your code, just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.

import random


def different_code():
    return random.randint(0,10)


file_name = str(input("The name of file: "))

with open(f'{file_name}.md', 'w') as open_file:
    open_file.write(str(different_code()))
