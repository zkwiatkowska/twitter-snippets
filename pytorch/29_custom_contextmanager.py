"""
Python tip for Machine Learning and PyTorch 💡

When I just started I was often forgetting to switch between train and eval modes in PyTorch. 😅

You can actually solve it using Python context managers and creating automatic switch. 👇
"""

import torch


class MyModel(torch.nn.Module):
    """Here is all the logic."""


class TrainingSession:
    def __init__(self, net: torch.nn.Module):
        self.net = net

    def __enter__(self):
        self.net.train()
        return

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.net.eval()


# loading a file
model = MyModel()
with TrainingSession(net=model) as f:
    print(model.training)

print(model.training)
