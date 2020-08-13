# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def is_palindrome(string):

    for i in range(len(string)):
        if not string[-i]==string[i-1]:
            return False
    return True

while True:
    print(is_palindrome(input("Is palindrome?: ")))
