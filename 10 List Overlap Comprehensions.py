import random

a = random.sample(range(1, 20), 12)
b = random.sample(range(1, 20), 16)
result_overlap = [i for i in set(a) if i in b]
print(result_overlap)
