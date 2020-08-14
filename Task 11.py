# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
#     You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.


def is_prime(num):
    d = 0
    for divisors in range(num):

        if num % (divisors + 1) == 0:
            d += 1

    if d <= 2:
        return True
    else:
        return False


for i in range(150):
    if is_prime(i) == True:
        print(f"{i} is prime number")