import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)  # [[1 2 3], [4 5 6]]

x[0, 1] = 5
print(x)  # # [[1 5 3], [4 5 6]]

x.flags.writeable = False
x[0, 1] = 2  # ValueError: assignment destination is read-only
