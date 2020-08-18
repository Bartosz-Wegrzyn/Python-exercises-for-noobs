happy_numbers = []
prime_numbers = []

with open('scr/happynumbers.txt', 'r') as happy:
    happy_numbers_line = happy.readline()

    while happy_numbers_line:
        happy_numbers_line = happy.readline()
        happy_numbers += happy_numbers_line

with open('scr/primenumbers.txt', 'r') as prime:
    prime_numbers_line = prime.readline()

    while prime_numbers_line:
        prime_numbers_line = prime.readline()
        prime_numbers += prime_numbers_line


# new_list = happy_numbers.append(prime_numbers)

# def first_way(a):
#     b = []
#     for i in range(len(a)):
#         if a[i] in b:
#             continue
#         else:
#             b.append(a[i])
#     print(b)
#
#
# first_way(new_list)

overlaplist = []
for elem in prime_numbers:
    if elem in happy_numbers:
        if elem == "\n":
            pass
        else:
            overlaplist.append(elem)

print(sorted(set(overlaplist)))