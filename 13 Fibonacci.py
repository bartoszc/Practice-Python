def fib(num):
    """Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
    Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number
    of numbers in the sequence to generate."""
    if num == 0 or num == 1:
        return 1
    else:
        tab = [1, 1, ]
        for i in range(1, num-1):
            tab.append(tab[i] + tab[i-1])
        return tab


print(fib(50))


