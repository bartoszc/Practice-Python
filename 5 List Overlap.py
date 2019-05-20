import random

print(set.intersection(set(random.randint(1, 100) for _ in range(30)), set(random.randint(1, 100) for _ in range(10))))
