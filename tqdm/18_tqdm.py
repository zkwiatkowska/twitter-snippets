"""
You don't need to print anything in your for loop to see how it progresses. 🔥

More elegant solution (imo) is to use tqdm and conveniently and quickly create a progress bar. 👇

And you will additionaly get the information how many iterations you do on avg in 1 second!
"""

from tqdm import tqdm

for _ in tqdm(range(100)):
    pass

# 100%|██████████| 100/100 [00:00<00:00, 2255002.15it/s]
