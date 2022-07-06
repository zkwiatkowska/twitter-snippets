import pandas as pd
import numpy as np

grades = pd.DataFrame({
    "name": np.random.choice(["Alice", "Bob", "Mark"], size=100),
    "grade": np.random.randint(low=1, high=7, size=100)
})

print(grades.describe().T)

#        count  mean       std  min  25%  50%  75%  max
# grade  100.0   3.3  1.772403  1.0  2.0  3.0  5.0  6.0

print(grades.groupby(by="name").describe())

#       grade
#       count      mean       std  min   25%  50%  75%  max
# name
# Alice  29.0  3.379310  1.934901  1.0  2.00  3.0  5.0  6.0
# Bob    32.0  2.812500  1.490562  1.0  1.75  2.5  4.0  5.0
# Mark   39.0  3.641026  1.813505  1.0  2.00  4.0  5.0  6.0
