import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 0], [0, 1]])

a * b  # not matrix multiplication - it will return element wise multiplication
np.matmul(a, b)  # matrix multiplication using function
a @ b  # matrix multiplication using operator
