"""
⏰ Python tip time!

If you're using pandas, this is a match made in heaven.

Apply + lambda = ❤️

Apply allows you to modify Series (and so a df column) and lambda - to quickly define how.

BUT!

If you use modification often, it may be better to define a proper function.
"""

import pandas as pd

a = pd.Series([1, 0, 0, 1, 0, 1, 1, 0, 1])

a = a.apply(lambda x: "dog" if x == 1 else "cat")
print(a.head(3))
#
# 0    dog
# 1    cat
# 2    cat
# dtype: object
