# import library for generating random numbers
import random

# create a variable and assign a random number between 1-5 everytime the program runs
number = random.randint(0, 11)
lives = 3

print('I am thinking of a number between 1 and 10')
print('You have three tries to guess the number.')

# logic loop to play as long as more than 0 lives left
while lives > 0:
    # collect user guess
    guess = int(input('Please choose a number: '))

    if guess == number:
        print('That is right!!')
    else:
        print('Try again')
        # every time the guess is wrong, remove one life
        lives = lives - 1
        print('Lives remaining: ' + str(lives))

print('Better luck next time!')
