"""
Watch out for this when multiplying matrices in numpy ‼️

Using asterisk (*) will only perform element-wise multiplication and won't give you desired result.

For actual matrix multiplication, you can use matmul or @. 🚀
"""

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 0], [0, 1]])

a * b  # NOT matrix multiplication - it will return element wise multiplication
np.matmul(a, b)  # matrix multiplication using function
a @ b  # matrix multiplication using operator
