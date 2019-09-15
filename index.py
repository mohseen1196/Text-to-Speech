from gtts import gTTS

import os

f=open("index.txt")
x=f.read()

language='en'

audio = gTTS(text=x,lang=language,slow=False)

audio.save("index.wav")

os.system("index.wav")
