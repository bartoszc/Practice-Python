guesses = 1
gn = 50
print('Think about random number in range 0 to 100 - I would try to guess it! ')
while True:
    print(f"It's {gn}?")
    answer = input('Guessed? (y), too low (l) or too high (h)? ')
    if answer == 'y':
        print(f"Yeah! Number of guesses {guesses}")
        break
    elif answer == 'l':
        gn += 10
    else:
        if guesses == 1:
            gn = 25
        else:
            gn -= 1
    guesses += 1


