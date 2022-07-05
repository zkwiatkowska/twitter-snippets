"""
Typing is an awesome way to keep track of what types we want to use in our functions' inputs and outputs. 🚀

We can use Optional if we want to pass a value or None, or even indicate how many values and of what types should a Tuple have.

And we can still use default values. 🔥
"""

from typing import Optional, Tuple


def my_function(a: float = 0.5, b: Optional[int] = None) -> Tuple[int, str]:
    """This way we can indicate what types we expect as input and output."""
