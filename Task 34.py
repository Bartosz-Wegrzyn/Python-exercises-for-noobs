import json

def look_for_birthday():
    with open("scr/birthday_dictionary.json", "r") as f:
        birthday_dictionary = json.load(f)
    print("We know the birthdays of: ")
    for people in birthday_dictionary:
        print(people)
    print("Who's birthday do you want to look up?")
    birthday_date_of = str(input())
    print(birthday_dictionary[birthday_date_of])

def add_record():
    with open('scr/birthday_dictionary.json', 'r+') as file:
        birthday_dictionary = json.load(file)

        name = input("Add full name: ")
        birthdate = input("Add birthdate: ")

        person = {name:birthdate}

        birthday_dictionary.update(person)
        file.seek(0)
        json.dump(birthday_dictionary, file)







print("Welcome to the birthday dictionary. ")
print("What do you need? ")
print("1 - look for birthday. 2 - add record to dictionary")

a = int(input())

if a == 1:
    look_for_birthday()
elif a == 2:
    add_record()

