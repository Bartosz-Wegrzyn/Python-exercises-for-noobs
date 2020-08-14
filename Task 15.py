# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to
# the user the same string, except with the words in backwards order. For example, say I type the string:

long_string = "Write a program (using functions!) that asks the user for a long string containing multiple words. " \
              "Print back to the user the same string, except with the words in backwards order. "
list_string = long_string.split(" ")
reverse = []

for i in range(len(list_string)):
    reverse.append(list_string[-i-1])

result = " ".join(reverse)
print(result)
