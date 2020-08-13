# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("Number: "))

for divisors in range(num):

    if num % (divisors + 1) == 0:
        print(divisors + 1)