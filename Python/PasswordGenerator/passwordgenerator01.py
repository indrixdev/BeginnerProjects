# import library for generating randoms
import random

# create a list of characters to be used when creating a password
characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_#*?!$%'

# ask user how many characters to make the password
password_length = int(input('Enter character limit for the password: '))

# generate the password
password = ''.join(random.sample(characters, password_length))

print(password)
