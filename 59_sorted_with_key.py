x = [(1, 2), (2, 3), (4, 1), (5, 2), (8, 0)]

sorting = sorted(x, key=lambda i: i[1])
print(sorting)

# [(8, 0), (4, 1), (1, 2), (5, 2), (2, 3)]
