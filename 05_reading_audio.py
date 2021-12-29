import soundfile as sf

my_audio, sampling_rate = sf.read("/home/zkwiatkowska/Desktop/datasets/dm_scholarship/fokkie/claustrophobia/Claustrofobia v1.1/Flower pot 2/POT2.wav")
print(my_audio.shape)
