import pandas as pd
import numpy as np

x = pd.Series(np.random.randint(1, 6, size=50))

print(x.head(2))

# 0    5
# 1    1
# dtype: int64

print(x.tail(2))

# 48    4
# 49    4
# dtype: int64
