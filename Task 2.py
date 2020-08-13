# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

while True:

    try:
        num = int(input("Give me number: "))
        if num%2 == 0:
            print(str(num) + " is even")
        else:
            print(str(num)+" is odd")
    except ValueError:
        continue