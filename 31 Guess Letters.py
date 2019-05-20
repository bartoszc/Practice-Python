import random


def random_word(file):
    with open(file) as f:
        content = f.readlines()
    return random.choice(content)


word = random_word('sowpods.txt')
so_far = '-' * len(word)
used = []
word = 'tata'

while so_far != word:
    print('Used letters: {}'.format(used))
    print(so_far)

    guess = input('Enter a letter: ')

    while guess in used:
        print('That letter was guessed by you already! ')
        guess = input('Enter a letter: ')

    used.append(guess)

    if guess in word:
        print('Yes, letter {} is in the magic word!'.format(guess))

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print('Letter {} isnt in the magic word'.format(guess))