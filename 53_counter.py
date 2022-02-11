from collections import Counter
from numpy import random

a = list(random.randint(low=1, high=10, size=100000))

count = Counter(a)

print(count)                   # Counter({3: 11259, 9: 11217, 1: 11181, 5: 11162, 7: 11103, ...})
print(count.most_common(2))    # [(3, 11259), (9, 11217)]
