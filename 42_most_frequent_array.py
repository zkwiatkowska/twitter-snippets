import numpy as np

a = np.random.randint(size=(10, 10), low=-1, high=5)

uniques, values = np.unique(a, return_counts=True)

print(uniques, values)                                  # [-1  0  1  2  3  4] [19 19 18 12 15 17]
print(uniques[np.where(values == np.max(values))])      # [-1  0]
