"""
⏰ Python tip time!

Do you know what's the difference between NumPy NaN and Inf?

Let's decompose this code in a thread. 👇🧵

Definitions!

NaN, or Not a Number, is a value which represents that something is undefined or can't be represented. 🤯

Inf is representation of mathematical concept of infinity. 📈

This already gives us a difference: inf describes a single concept, while nan - set of them.

Now let's see couple of first lines. 👇

You can see the difference that matches our conclusion from definition.

When comparing infs, we see they "are equal", meaning represent single concept. With NaN, it's not the case, because this is not a representation of a single idea.

Because NaN is not a single idea, NumPy allows us to check:

➡️ NOT if something equals NaN,
➡️ BUT if an operation results in a NaN.

By calculating logarithm of a negative number, we end up with NaN, because logarithm does not even take into account negatives as arguments.

However!

What about some operations on values that are close enough to function arguments?

Well, it appears that NumPy is smart and we can obtain limits of the function.

In this case, limit of logarithm when x approaches 0 is -inf.

So finally, it's good to remember inf is not a NaN.

And here's some code to confirm it. 👇
"""

import numpy as np

print(np.nan == np.nan)          # FALSE
print(np.inf == np.inf)          # TRUE

print(np.nan == np.log(-1))      # FALSE
print(np.isnan(np.log(-1)))      # TRUE

print(-np.inf == np.log(0))      # TRUE

print(np.isnan(np.inf))          # FALSE
