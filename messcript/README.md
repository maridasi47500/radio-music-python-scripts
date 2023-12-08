I think we need a bit more information about your audio files. Try converting them to wav files instead of using mp3. This may work better for you.

ffmpeg -i input.mp3 output.wav  
 or lance
./changetone.sh in.mp4
 ou
./changetone.sh in.mp3


puis

python3 tone.py in.wav a g#de la à sol

python3 tone.py in.wav e #de mi


puis pluslent_script.py in.wav [speed entre -1 et 1]
