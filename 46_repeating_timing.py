from itertools import repeat
from timeit import timeit

size = 10000000
value = 1000

print(timeit(lambda: list(repeat(value, size)), number=100))     # Time: 4.916 s on average
print(timeit(lambda: [value] * size, number=100))                # Time: 3.199 s on average

print(timeit(lambda: repeat(value, size), number=100))           # Time: 0.0000142 s on average
