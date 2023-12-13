from scipy.io import wavfile
import scipy
import librosa, numpy as np
import sys
import pydub

hey=sys.argv[1]
hi=sys.argv[2]

song, fs = librosa.load(hey)
filename=hey.split("/")[-1]


song_2_times_faster = librosa.effects.time_stretch(song, rate=float(hi))

scipy.io.wavfile.write("./uploads/faster_"+str(hi)+"_"+filename, fs, song_2_times_faster) # save the song

