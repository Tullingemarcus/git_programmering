
from gtts import gTTS

import os





mytext = input("skriv in något här: ")

language = 'sv'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("welcome.mp3")

