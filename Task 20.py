import time

a = []
for i in range(19_000_000):
    a.append(i)

def binary_search(list, element):
    middle_element_index = len(list) // 2
    middle_element = list[len(list) // 2]

    if len(list) - 1 > 0:

        if element == middle_element:
            print(f"Element {element} is in list")
        elif element < middle_element:
            binary_search(list[:middle_element_index], element)
        elif element > middle_element:
            binary_search(list[middle_element_index:], element)

    else:
        print(f"Element {element} is not in list")
        return None


def linear_search(list, element):
    for i in range(len(list)):
        if element == list[i]:
            return True




start = time.time()
binary_search(a, 18_900_000)
end = time.time()
print(end - start)


start = time.time()
print(linear_search(a, 18_900_000))
end = time.time()
print(end - start)



