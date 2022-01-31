import numpy as np

x = np.random.rand(10)

a = x - np.mean(x) + 0.231
b = x + 0.231 - np.mean(x)

print(np.array_equal(a, b))
print(np.allclose(a, b))
