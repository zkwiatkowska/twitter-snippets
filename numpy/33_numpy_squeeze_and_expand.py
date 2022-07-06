"""
⏰ Python tip for ML!

When implementing neural nets we sometimes have to create artificial dimensions or remove them so the input matches the requirements.

Example: processing audio as image in CNN

Two functions that come in handy for that are: expand_dims and squeeze. 👇
"""

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)                              # (2, 3)

a = np.expand_dims(a, axis=0)
print(a.shape)                              # (1, 2, 3)

a = a.squeeze()
print(a.shape)                              # (2, 3)
