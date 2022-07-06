"""
⏰ Python tip time!

Remember our friend tqdm?

It allowed us to quickly create progress bars to measure execution of our "for" loops (see the comment for reminder). 🚀

But! If you use it together with range function, tqdm provides us with a convenient wrapper for it. 👇
"""

from tqdm import tqdm, trange

for i in tqdm(range(100)):
    pass

for i in trange(100):
    pass
