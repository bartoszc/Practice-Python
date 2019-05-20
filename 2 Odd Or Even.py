num = int(input('Enter the number: '))
check = int(input('Enter second number: '))

print('Even') if num % 2 == 0 else print('Odd')
if num % 4 == 0:
    print('Multiple of 4')

print('Divisible by', check) if num % check == 0 else print('Not divisible by', check)
