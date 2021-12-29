import numpy as np

arr = np.array([1, 2, 3, 4])

a = np.pad(arr, pad_width=(2, 2), mode="constant", constant_values=1)  # [1 1 12 3 4 1 1]
b = np.pad(arr, pad_width=(2, 2), mode="edge")  # [1 1 1 2 3 4 4 4]
c = np.pad(arr, pad_width=(2, 2), mode="reflect")  # [3 2 1 2 3 4 3 2]
d = np.pad(arr, pad_width=(2, 2), mode="symmetric") # [2 1 1 2 3 4 4 3]
e = np.pad(arr, pad_width=(2, 2), mode="wrap")  # [3 4 1 2 3 4 1 2]
f = np.pad(arr, pad_width=(2, 2), mode="linear_ramp", end_values=(-1, 6))  # [-1 0 1 2 3 4 5 6]
