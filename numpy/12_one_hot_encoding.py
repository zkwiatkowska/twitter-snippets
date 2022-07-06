"""
Creating a one hot encoded vector with labels is used often across ML field.

❓ Do you know how to quickly do it in plain Python, numpy and pytorch?

Here is the example, but try yourself first! 👇
"""

import numpy as np
import torch
from torch.nn.functional import one_hot

k = 5  # position of 1
n = 10  # number of classes

a = [1 if i == k else 0 for i in range(n)]              # in plain Python
b = np.insert(np.zeros(shape=n-1, dtype=int), k, 1)     # in numpy
c = one_hot(torch.tensor([k]), n)                       # in pytorch
