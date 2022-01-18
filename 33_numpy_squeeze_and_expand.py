import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)                              # (2, 3)

a = np.expand_dims(a, axis=0)
print(a.shape)                              # (1, 2, 3)

a = a.squeeze()
print(a.shape)                              # (2, 3)
