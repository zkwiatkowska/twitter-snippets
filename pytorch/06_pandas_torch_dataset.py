"""
How to create custom pytorch dataset with data from pandas frame? 🚀

We can easily create pytorch dataset by simply implementing 2 methods:

1. __getitem__ - tells us how to construct i-th example (use .iloc and .values to get array),
2. __len__ - tells us how long dataset is.
"""

from torch.utils.data import Dataset
import pandas as pd


class MyFrameAsDataset(Dataset):

    def __init__(self, path_to_df):
        self.df = pd.read_csv(path_to_df)

    def __getitem__(self, item):
        return self.df.iloc[item].values

    def __len__(self):
        return len(self.df)


print(MyFrameAsDataset("my_frame.csv")[5])
