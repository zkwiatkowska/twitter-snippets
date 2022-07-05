"""
One of the simplest way to read .wav file in Python is using soundfile library. 🎵

Its read method returns a tuple with:
1. audio as numpy array,
2. sampling rate as int.

Sampling rate can tell us about the quality of recording and it tells how many samples were collected in 1 second.

For example SR of 44100 tells us we will have 44100 numbers for each 1 second of audio.

The higher the value, the more variety is recorded in our file.

Audio numpy array is of shape (length, channels).

If our SR is 44100 and we have 10 second of audio, our length will be simply 44100 * 10 = 441000.

What about channels?

It tells us how many tracks were used to record our file. For example stereo will have 2 channels.
"""

import soundfile as sf

my_audio, sampling_rate = sf.read("my/audio/file.wav")
print(my_audio.shape)
