"""
Python tip for Data Scientists 🐍

When creating a dataset or saving logs from experiment, we often want our files to follow the same pattern, for example:

file001_bark_44100.wav

We can easily verify if they do using Python regular expressions and re.fullmatch() function. 👇
"""

import re

# We want to verify if all files have the same pattern f(code)_(length)_(name).wav
# code is exactly 3 digit number
# length is a number consisting of 1 to 3 digits
# name is a string consisting of 1 to 5 lowercase characters
# all files start with f, end with .wav, and have _ as a separator

files = ["f123_12_bark.wav", "243_11_glass.wav", "f123_11_12.wav", "f123+12+bark.wav"]
pattern = "^f[0-9]{3}_[0-9]{1,3}_[a-z]{1,5}.wav"

for file in files:
    if re.fullmatch(pattern, file) is None:
        print(file)

# We find that "243_11_glass.wav", "f123_11_12.wav" and "f123+12+bark.wav" does not conform.
