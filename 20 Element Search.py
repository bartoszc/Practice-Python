def check(arr, num):
    """Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
    largest) and another number. The function decides whether or not the given number is inside the list and returns
    (then prints) an appropriate boolean."""
    return num in sorted(arr)


def check_binary(arr, num):
    arr.sort()
    while True:
        middle = len(arr) // 2
        if num >= arr[middle]:
            arr = arr[middle:]
        else:
            arr = arr[:middle]
        if len(arr) == 1:
            return True if arr[0] == num else False


# print(check([1, 5, 2, 8, 7, 6, 3, 1, 4], 5))
# print(check_binary([1, 3, 5, 30, 42, 43, 500], 9))
l = [2, 4, 6, 8, 10]
print(check_binary(l, 5))  # prints False
print(check_binary(l, 10))  # prints True
print(check_binary(l, -1))  # prints False
print(check_binary(l, 2))  # prints True