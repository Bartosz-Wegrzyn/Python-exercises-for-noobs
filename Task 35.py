import json

months_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
months = {
    "January": 0,
    "February": 0,
    "March": 0,
    "April": 0,
    "May": 0,
    "June": 0,
    "July": 0,
    "August": 0,
    "September": 0,
    "October": 0,
    "November": 0,
    "December": 0,
}

with open("scr/birthday_dictionary.json", "r") as f:
    birthday_dictionary = json.load(f)

for people in birthday_dictionary:
    a = birthday_dictionary[people]
    month = int(a[5:7])

    months[months_names[month]] += 1

for i in months:
    print(i, end=" ")
    print(months[i])
