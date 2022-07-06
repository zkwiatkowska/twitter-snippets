from collections import defaultdict

x = defaultdict(lambda: 5)

print(x)

x["a"] = f"The default key was {x[2]} all along."
x[1] **= 2

print(x)

y = defaultdict(int)
z = defaultdict(list)
