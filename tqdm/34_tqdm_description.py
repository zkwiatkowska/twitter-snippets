"""
โฐ Python tip time!

Using too many tqdm progress bars and getting lost which is which?

Name them!

You can use "desc" argument to name your progress bar and keep everything clean and tidy. ๐งน

Do you remember what did the "trange" function do? ๐ง
"""

from tqdm import trange

for _ in trange(100, desc="My progress bar"):
    pass

# My progress bar: 100%|โโโโโโโโโโ| 100/100 [00:00<00:00, 2892623.45it/s]
