import pandas as pd

dummy_series = pd.Series(["Mark", "Bob", "Alice", "Mark", "Bob", "Anna", "Bob"])
dummy_series.value_counts()

# Bob      3
# Mark     2
# Alice    1
# Anna     1

