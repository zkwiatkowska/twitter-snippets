import pandas as pd
from tqdm.auto import tqdm

x = pd.DataFrame({"a": [1, 2] * 30})

tqdm.pandas()
x["b"] = x["a"].progress_apply(lambda i: "a" if i == 1 else "b")

# 100%|██████████| 60/60 [00:00<00:00, 264346.89it/s]
