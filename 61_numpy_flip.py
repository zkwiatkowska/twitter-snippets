import numpy as np

x = np.diag([1] * 3)
print(x)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

y = np.flip(x, axis=0)
print(y)
# [[0 0 1]
#  [0 1 0]
#  [1 0 0]]
