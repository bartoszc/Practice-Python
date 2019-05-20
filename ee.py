def odd_count(n):
    return len(tuple(x for x in range(n) if x % 2 != 0))


print(odd_count(15))
print(odd_count(15023))