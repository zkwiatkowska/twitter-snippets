from collections import OrderedDict

{"a": 1, "b": 2} == {"b": 2, "a": 1}              # TRUE
OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1)    # FALSE !!
