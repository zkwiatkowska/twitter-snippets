import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()

x = np.linspace (-5, 5, 100)
y = x ** 3 + 2 * x ** 2 + 5 * x + 1

plt.plot(x, y)
plt.title("This was done with matplotlib!!!")
plt.show()
