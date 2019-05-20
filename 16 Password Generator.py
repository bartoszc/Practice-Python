import random


def pass_gen():
    """Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix
    of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
    password every time the user asks for a new password. Include your run-time code in a main method."""
    q = input('You want a strong or weak password? (w - weak, s - strong) ')
    if q.lower() == 'w':
        pas = ('typo', 'abcd', 'ala', 'kota')
        return random.choice(pas)
    else:
        new_p = []
        for i in range(4):
            new_p.append(random.choice(list(map(chr, range(97, 123)))))
        for i in range(4):
            new_p.append(random.choice(list(map(chr, range(65, 91)))))
        for i in range(3):
            new_p.append(random.choice(list(map(chr, range(33, 48)))))
        for i in range(4):
            new_p.append(str(random.randint(1, 9)))
        random.shuffle(new_p)
        return ''.join(new_p)


print(pass_gen())
