from itertools import cycle

values = cycle(["even", "odd"])

for i in range(5):
    print(f"{i} is {next(values)} number")

# 0 is even number
# 1 is odd number
# 2 is even number
# 3 is odd number
# 4 is even number
