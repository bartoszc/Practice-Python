# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input('Enter a number: '))
print(list([x for x in range(1, num+1) if num % x == 0]))