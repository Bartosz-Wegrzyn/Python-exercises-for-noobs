# Implement a function that takes as input three variables, and returns the largest of the three. Do this without
# using the Python max() function! The goal of this exercise is to think about some internals that Python normally
# takes care of for us. All you need is some variables and if statements!

a = 11
b = 11
c = 9
max = None

def max_num(a, b, c):
    if a > b:
        if a > c:
            max = a
        elif a < c:
            max = c
        elif a == c:
            mac = c

    elif a < b:
        if b > c:
            max = b
        elif b < c:
            max = c
        elif b == c:
            max = c
    elif a == b:
        max = a


    return max

print(max_num(a, b, c))