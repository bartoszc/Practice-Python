def is_prime(num=1):
    return True if len([x for x in range(1, num + 1) if num % x == 0]) <= 2 else False


print(is_prime(7))
