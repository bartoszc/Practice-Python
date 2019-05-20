"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
whether they guessed too low, too high, or exactly right."""

import random

rn = random.randint(1, 9)
guesses = 0

while True:
    i = input('Enter a number between 1 and 9: ')
    guesses += 1
    if i == 'exit':
        print('You stopped the game')
        break
    elif int(i) == rn:
        print(f'You were right! The magic number is: {rn} and the number of guesses is {guesses}')
        break
    elif int(i) > rn:
        print('Too high!')
    else:
        print('Too low!')






