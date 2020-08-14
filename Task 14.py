# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

####### 1 way ##########
def first_way(a):
    b = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.append(a[i])
    print(b)

def sec_way(a):
    print(sorted(set(a)))

first_way(a)
sec_way(a)