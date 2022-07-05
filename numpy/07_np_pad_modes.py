"""
One of my all time favourite things to use in numpy is its "pad" method. 🚀

Pad allows you to extend your array to the new size, for example from array of length 5 to array of length 10.

But there are various ways of filling the values. Here's explanation of some of them. ⤵️

But first - the setup.

Let's focus on 1 dimension only.

As you can see, we have to specify how we want to pad our array, by saying how much we want to expand it (on the left, and on the right).

For now we will pad it with 2 values on both sides.

The most natural way is to pad it with a constant value everywhere.

If we didn't state the value or multiple values to use, a default action would be to pad everything with zeros.

Another straightforward way would be to use edge values as fillers.

In our array, we had 1 in the beginning and 4 in the end, so we simply use them to perform padding.

Reflect and symmetric are better analysed together.

Imagine that we could pad our array by putting a mirror on both sides. A mirror on the left side could show our array in reverse order.

But here's the catch! It depends where we put the mirror.

In reflect, we put our mirror *in the array*.

This is why we don't duplicate thr first and the last value, but we just use next ones.

In symmetric however, we put our mirror *outside of the array*.

This is why our mirror reflects also the first and the last value and duplicates them symmetrically.

Wrap is actually my favourite.

You can imagine you copy your array on the left and on the right, and then cut it with additional elements on both sides.

This is why on the left we added [3 4] - it's because we would copy and cut like this: [1 2 cut [3 4 1 2 3 4]
"""

import numpy as np

arr = np.array([1, 2, 3, 4])

a = np.pad(arr, pad_width=(2, 2), mode="constant", constant_values=1)  # [1 1 1 2 3 4 1 1]
b = np.pad(arr, pad_width=(2, 2), mode="edge")  # [1 1 1 2 3 4 4 4]
c = np.pad(arr, pad_width=(2, 2), mode="reflect")  # [3 2 1 2 3 4 3 2]
d = np.pad(arr, pad_width=(2, 2), mode="symmetric") # [2 1 1 2 3 4 4 3]
e = np.pad(arr, pad_width=(2, 2), mode="wrap")  # [3 4 1 2 3 4 1 2]
f = np.pad(arr, pad_width=(2, 2), mode="linear_ramp", end_values=(-1, 6))  # [-1 0 1 2 3 4 5 6]
