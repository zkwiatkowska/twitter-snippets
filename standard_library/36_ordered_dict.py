"""
⏰ Python tip time!

Since Python 3.7, dict in Python preserves keys' order.

Does it mean OrderedDict is redundant then? 🧐

Not at all!

If you want to use comparison in your code, it's still useful to use OrderedDict. 👇

Also - by using it you show exactly what you meant.
"""

from collections import OrderedDict

{"a": 1, "b": 2} == {"b": 2, "a": 1}              # TRUE
OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1)    # FALSE !!
