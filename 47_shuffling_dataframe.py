import pandas as pd

x = pd.Series(range(50))

x.sample(n=len(x))
