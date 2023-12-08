from scipy.io import wavfile
import scipy
import librosa, numpy as np
import sys
import pydub


song, fs = librosa.load(sys.argv[1])

song_2_times_faster = librosa.effects.time_stretch(song, rate=float(sys.argv[2]))

scipy.io.wavfile.write("song_2_times_faster.wav", fs, song_2_times_faster) # save the song

