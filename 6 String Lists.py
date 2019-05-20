def palindrome(text):
    """Ask the user for a string and print out whether this string is a palindrome or not.
    (A palindrome is a string that reads the same forwards and backwards.)"""
    return text[::-1] == text


print(palindrome('assa'))
