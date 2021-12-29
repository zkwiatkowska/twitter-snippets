from itertools import product

batch_sizes = [8, 16, 32]
shuffle_options = [True, False]
learning_rates = [1e-3, 1e-4, 1e-5]

product(batch_sizes, shuffle_options, learning_rates)

#  [(8, True, 0.001), (8, True, 0.0001), ... ]
