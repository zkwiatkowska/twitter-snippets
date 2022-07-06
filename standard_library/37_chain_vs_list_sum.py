"""
⏰ Python tip time!

How would you perform list concatenation if you had a lot of them?

One way is using a regular addition operator. ➕

If we used chain, we could have some substantial gains time-wise.

(to make it fair, I converted chain to list to result in the same object)
"""

from itertools import chain
from timeit import timeit

a = b = c = d = e = f = list(range(1000000))

print(timeit(lambda: a + b + c + d + e + f, number=100))
print(timeit(lambda: list(chain(a, b, c, d, e, f)), number=100))

# 11.653475503999744
# 5.214757513000222
