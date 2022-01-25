import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 6, 7], [4, 5, 6]])
print(a)

# [[1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 6 7]
#  [4 5 6]]

print(np.unique(a, axis=0))

# [[1 2 3]
#  [4 5 6]
#  [4 6 7]]
