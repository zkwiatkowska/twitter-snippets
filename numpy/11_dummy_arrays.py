"""
Creating dummy numpy arrays can come in handy when debugging your code. ‼️

Here are some various ways to do it quickly 👇
"""

import numpy as np

np.random.rand(2, 3)                                # random floats between 0 and 1
np.zeros((2, 3))                                    # filled with zeros
np.ones((2, 3))                                     # filled with ones
np.random.randint(low=0, high=10, size=(2, 3))      # random integers between 0 and 10
np.empty((2, 3))                                    # empty array
np.full(shape=(2, 3), fill_value=2)                 # filled with specified value
