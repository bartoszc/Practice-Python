birthdays = {'Albert Einstein': '14.03.1879',
             'Benjamin Franklin': '17.01.1706',
             'Abraham Lincoln': '12.02.1809'}

print(f'Welcome to the birthday dictionary. We know the birthdays of: ')
for key in birthdays.keys():
    print(key)

who = input("Who's birthday do you want to look up? ")
print('The birthday of {} is {}'.format(who, birthdays[who])) if who in birthdays else print('I dont know him')


