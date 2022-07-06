import numpy as np

x = np.fromfunction(lambda i, j: i * j, shape=(5, 5), dtype=int)
print(x)

# [[ 0  0  0  0  0]
#  [ 0  1  2  3  4]
#  [ 0  2  4  6  8]
#  [ 0  3  6  9 12]
#  [ 0  4  8 12 16]]
