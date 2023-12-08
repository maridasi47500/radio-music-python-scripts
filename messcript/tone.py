from pydub import AudioSegment
import sys

import numpy as np
from numpy.random import uniform
tones=["f","f#","g","g#","a","a#","b","c","c#","d","d#","e","f","f#","g","g#","a","a#","b","c","c#","d","d#","e","f"]
filename = sys.argv[1]
ton_a = sys.argv[2]
ton_b = sys.argv[3]
higher=True
try:
    x=ton_b.index("-")
    ton_b=ton_b.replace("-","")
    higher=False
except:
    higher=True
sound = AudioSegment.from_file(filename, format=filename[-3:])
tones=["f","f#","g","g#","a","a#","b","c","c#","d","d#","e"]
my_i=tones.index(ton_a)
i=0
mytones=[]
for tone in range(0,len(tones)):
    try:
        if my_i < len(tones):
          mytones.append(tones[my_i])
          #mytones.append(i)
        else:
          my_i=0
          mytones.append(tones[my_i])
          #mytones.append(i)
        my_i+=1
    except:
        print("error")



tones=mytones
print(tones)

octaves = 0.5#octve
#octaves = -0.25#quarte

#counter=0
counter=0
def rindex(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1
#for octaves in np.linspace(-1,1,25):
print("tonb", ton_b)
if higher == True:

    myton=tones.index(ton_b)+12
    octaves=np.linspace(-1,1,25)[myton]
    print(octaves)
else:
    myton=tones.index(ton_b)

    octaves=np.linspace(-1,1,25)[myton]
new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
hipitch_sound = hipitch_sound.set_frame_rate(44100)
#ort / save pitch changed sound
print(ton_b)
mynote=tones[counter]
print(counter)
hipitch_sound.export(f"octave_{ton_b}_{octaves}.wav", format="wav")
try:

  counter+=1
  

except Exception as e:
  print(e, "oops")
  counter=0
  #print(tones[counter])


