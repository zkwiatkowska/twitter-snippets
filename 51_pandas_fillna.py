import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
        ["A", .2, 1],
        ["B", np.nan, np.nan],
        [np.nan, 1.7, 8],
        ["C", 1.3, 11]
    ],
    columns=["col1", "col2", "col3"]
)

print(df.fillna(1))

#   col1  col2  col3
# 0    A   0.2   1.0
# 1    B   1.0   1.0
# 2    1   1.7   8.0
# 3    C   1.3  11.0

print(df.fillna(method="backfill"))
#
#   col1  col2  col3
# 0    A   0.2   1.0
# 1    B   1.7   8.0
# 2    C   1.7   8.0
# 3    C   1.3  11.0

print(df.fillna(method="ffill"))

#   col1  col2  col3
# 0    A   0.2   1.0
# 1    B   0.2   1.0
# 2    B   1.7   8.0
# 3    C   1.3  11.0

print(df.fillna(method="ffill", axis=1))

#   col1 col2  col3
# 0    A  0.2   1.0
# 1    B    B     B
# 2  NaN  1.7   8.0
# 3    C  1.3  11.0

print(df.fillna({"col1": "D", "col2": .3}))

#   col1  col2  col3
# 0    A   0.2   1.0
# 1    B   0.3   NaN
# 2    D   1.7   8.0
# 3    C   1.3  11.0

print(df.fillna(0, downcast="infer"))

#   col1  col2  col3
# 0    A   0.2     1
# 1    B   0.0     0
# 2    0   1.7     8
# 3    C   1.3    11
