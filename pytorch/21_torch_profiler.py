"""
Wondering why your PyTorch code is slow and want to find a bottleneck? 🧐

You can use a built-in profiler in 3 steps! 🚀
-> wrap codes of interest in contexts
-> run model
-> check efficiency

(I omitted some obvious parts of the code for better visibility of profiler parts)
"""

import torch
from torch import nn
import torch.autograd.profiler as profiler


class MyModel(nn.Module):

    def __init__(self, channels_in, channels_out):
        super(MyModel, self).__init__()
        self.conv = nn.Conv2d(in_channels=channels_in, out_channels=8, kernel_size=(3, 3))
        self.dense = nn.Linear(8, channels_out)

    def forward(self, x):
        with profiler.record_function("conv block"):
            x = self.conv(x)
            x = torch.mean(x, [-1, -2])

        with profiler.record_function("linear block"):
            x = self.dense(x)

        return x


if __name__ == '__main__':
    model = MyModel(1, 1)
    dummy_input = torch.rand(1, 1, 20, 20)

    with profiler.profile() as prof:
        model(dummy_input)

print(prof.table(sort_by="self_cpu_time_total"))

# ------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
#                           Name    Self CPU %      Self CPU   CPU total %     CPU total  CPU time avg    # of Calls
# ------------------------------  ------------  ------------  ------------  ------------  ------------  ------------
#      ...
#                     conv block        14.44%     164.000us        84.33%     958.000us     958.000us             1
#                   linear block         4.23%      48.000us        12.06%     137.000us     137.000us             1
#      ...
