import json

with open('info.json', 'r') as f:
    info = json.load(f)

who = input("Who's birthday do you want to look up? ")

try:
    print('The birthday of {} is {}'.format(who, info[who]))
except KeyError:
    print('I dont know him')

new_name = input('Enter name of new person: ')
bdate = input('..And date of birth: ')

info[new_name] = bdate

with open('info.json', 'w') as f:
    json.dump(info, f)


