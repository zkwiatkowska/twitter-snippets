import pandas as pd

df = pd.Series(["a_2", "b_1", "c_2", "d_3", "e_5", "g_3"])

df2 = df.str.split("_", expand=True)
print(df2)

#    0  1
# 0  a  2
# 1  b  1
# 2  c  2
# 3  d  3
# 4  e  5
# 5  g  3
