from scipy.io import wavfile
from vitesse import Vitesse
from chaine import Chaine
import scipy
from tonalite import Tonalite
from vitesse import Vitesse
import librosa, numpy as np
import sys
import pydub

hey=sys.argv[1]
hi=sys.argv[2]

song, fs = librosa.load(hey)
filename=hey.split("/")[-1]
myfilename=Chaine().fichier("hey.wav")
tonaliteid=Tonalite().getbyfiles(hey.split("/")[-1])["id"]
vitesse=Vitesse().create({"tonalite_id":tonaliteid,"vitesse":hi,"file":myfilename})


song_2_times_faster = librosa.effects.time_stretch(song, rate=float(hi))

scipy.io.wavfile.write("./uploads/"+myfilename, fs, song_2_times_faster) # save the song

