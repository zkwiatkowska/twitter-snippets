"""
⏰ Python tip time!

Using too many tqdm progress bars and getting lost which is which?

Name them!

You can use "desc" argument to name your progress bar and keep everything clean and tidy. 🧹

Do you remember what did the "trange" function do? 🧐
"""

from tqdm import trange

for _ in trange(100, desc="My progress bar"):
    pass

# My progress bar: 100%|██████████| 100/100 [00:00<00:00, 2892623.45it/s]
