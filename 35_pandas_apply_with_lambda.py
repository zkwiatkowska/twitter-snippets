import pandas as pd

a = pd.Series([1, 0, 0, 1, 0, 1, 1, 0, 1])

a = a.apply(lambda x: "dog" if x == 1 else "cat")
print(a.head(3))
#
# 0    dog
# 1    cat
# 2    cat
# dtype: object
