import pandas as pd
from random import random
import matplotlib.pyplot as plt

plt.style.use("ggplot")

x = [0]
for i in range(99):
    x.append(0.2 * x[i-1] - 0.1 + random())

x = pd.Series(x)
y = x.rolling(7).mean()

x.plot(color="black")
y.plot(color="red")
plt.savefig("roll.png", size=(10, 6), dpi=800)
