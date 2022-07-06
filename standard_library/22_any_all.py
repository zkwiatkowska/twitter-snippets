"""
One of the must-know Python goodies are its built-in functions: all and any. 🧐

1️⃣ Any verifies if "any item matches my condition" - below we check if any number in the list is greater than 2.

*️⃣ All verifies if "all item match my condition" - here all of them are integers.
"""

x = [1, 2, 3, 4, 5]

any(i >= 2 for i in x)                  # this is True because we have 1 and 2 in the list
all(isinstance(i, int) for i in x)      # this is True because all of them are integers
