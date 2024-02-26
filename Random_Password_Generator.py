# This program creates a 16 digit password generator

# Importing the random library so the password will be randomly generated
import random

# Output
print("Your password: ")

# Criteria for acceptable characters to be used for password
chars = "abcdefghijklmnopqrstuvwxyz1234567890!#$%&*"

# We want our password variable to be a blank string
# Created a For Loop to randomly choose password within the chars variable range
password = " "
for x in range(16):
    password += random.choice(chars)

print(password)
