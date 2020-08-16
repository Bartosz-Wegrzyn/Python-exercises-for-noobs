a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
     31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


def binary_search(list, element):
    middle_element_index = len(list) // 2
    middle_element = list[len(list) // 2]

    if len(list) - 1 > 0:

        if element == middle_element:
            print("TRUE")  # it is reaches to this point
            return True  # But it doesn't return TRUE
        elif element < middle_element:
            binary_search(list[:middle_element_index], element)
        elif element > middle_element:
            binary_search(list[middle_element_index:], element)

    else:
        return binary_search([1],1)


# print(binary_search(a, 25))  # return None
print(binary_search(a, 13))  # RecursionError
