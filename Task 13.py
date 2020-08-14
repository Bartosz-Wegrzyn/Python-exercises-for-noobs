# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
# opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in
# the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8,
# 13, …)
def fib_number(n):

        if n == 0:
            return(0)
        elif n == 1:
            return(1)
        elif n > 1:
            return(fib_number(n-1)+fib_number(n-2))


for fib in range(21):
    print(fib_number(fib))