# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
# password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

password_source = "!@#$%^&*()qwertyuiopasdfghjklzxcvbnm_-QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
password_list = []

for i in range(8):
    choice = random.randint(0,73)
    password_list.append(password_source[choice])

password = "".join(password_list)

print(password)
