import numpy as np
import torch
from torch.nn.functional import one_hot

k = 5  # position of 1
n = 10  # number of classes

a = [1 if i == k else 0 for i in range(n)]  # python list of ints
b = np.insert(np.zeros(shape=n-1, dtype=int), k, 1)  # numpy array of ints
c = one_hot(torch.tensor([k]), n)  # torch tensor of ints
