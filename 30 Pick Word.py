import random


def random_word(file):
    with open(file) as f:
        content = ''.join(f.readlines())
    return random.choice(content)


print(random_word('sowpods.txt'))
