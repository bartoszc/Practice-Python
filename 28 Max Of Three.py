def check(n1, n2, n3):
    largest = n1
    if n2 > largest:
        largest = n2
    if n3 > largest:
        largest = n3
    return largest


print(check(3, 5, 1))
