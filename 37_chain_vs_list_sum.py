from itertools import chain
from timeit import timeit

a = b = c = d = e = f = list(range(1000000))

print(timeit(lambda: a + b + c + d + e + f, number=100))
print(timeit(lambda: list(chain(a, b, c, d, e, f)), number=100))

# 11.653475503999744
# 5.214757513000222
