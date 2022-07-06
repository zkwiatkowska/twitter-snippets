"""
Pandas groupby is one of the best ways to create summaries with respect to some categorical variable. 🚀

Imagine you have a list of students and their grades.

You can then group your data frame by students and calculate their GPA. 👇
"""

import pandas as pd

df = pd.DataFrame([["Bob", 5.5], ["Bob", 1.2], ["Alice", 4.0], ["Bob", 4.8], ["Alice", 3.9], ["Alice", 5.2]],
                  columns=["Name", "Grade"])

#     Name  Grade
# 0    Bob    5.5
# 1    Bob    1.2
# 2  Alice    4.0
# 3    Bob    4.8
# 4  Alice    3.9
# 5  Alice    5.2

df.groupby(by="Name")["Grade"].mean()

# Alice    4.366667
# Bob      3.833333
