"""
If you are using Latex to create reports, theses or papers, and you're simultaneously using Python pandas - this is for you. 👇

Pandas has a built-in way to transform your Data Frame into a string with Latex table syntax. 🔥
"""

import pandas as pd

df = pd.DataFrame([["Bob", 5.5], ["Bob", 1.2], ["Alice", 4.0]], columns=["Name", "Grade"])
df.to_latex()

# \begin{tabular}{llr}
# \toprule
# {} &   Name &  Grade \\
# \midrule
# 0 &    Bob &    5.5 \\
# 1 &    Bob &    1.2 \\
# 2 &  Alice &    4.0 \\
# \bottomrule
# \end{tabular}
