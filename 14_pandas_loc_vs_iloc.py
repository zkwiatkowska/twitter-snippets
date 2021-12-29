import pandas as pd

dummy_series = pd.Series(["Anna", "Bob", "Alice", "Mark"], index=[2, 0, 1, 3])

# 2     Anna
# 0      Bob
# 1    Alice
# 3     Mark

dummy_series.loc[0]  # this results in "Bob", because "Bob" is located in index *of name* 0
dummy_series.iloc[0]  # this results in "Anna", because "Anna" is located in *position* 0
