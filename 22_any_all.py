x = [1, 2, 3, 4, 5]

any(i >= 2 for i in x)  # this is True because we have 1 and 2 in the list
all(isinstance(i, int) for i in x)  # this is True because all of them are integers
