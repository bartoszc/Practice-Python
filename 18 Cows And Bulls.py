import random


num = str(random.randint(1000, 9999))
cows = 0
bulls = 0

while True:
    guess = input('Enter your 4 digit guess number: ')
    if guess == num:
        print('Done!')
        break
    else:
        for i in range(4):
            if guess[i] == num[i]:
                cows += 1
            elif guess[i] in num:
                bulls += 1
        print(f"The secret number was {num}. Your score: {cows} cows, {bulls} bulls")


