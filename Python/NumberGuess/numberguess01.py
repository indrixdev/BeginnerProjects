# import library for generating random numbers
import random

# create a variable and assign a random number between 1-5 everytime the program runs
number = random.randint(0, 6)

print('I am thinking of a number between 1 and 5')

# collect user guess
guess = int(input('Please choose a number: '))

if guess == number:
    print('That is right!!')
else:
    print('Better luck next time!')
