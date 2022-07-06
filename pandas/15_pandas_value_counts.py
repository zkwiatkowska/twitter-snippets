"""
Do you want to quickly count occurrences of unique values in pandas Series or Data Frame column? 🧐

There's no easier way to do it than using a built-in value_counts method. 👇
"""

import pandas as pd

dummy_series = pd.Series(["Mark", "Bob", "Alice", "Mark", "Bob", "Anna", "Bob"])
dummy_series.value_counts()

# Bob      3
# Mark     2
# Alice    1
# Anna     1

