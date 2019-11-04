from gtts import gTTS

import os


def translate(phrase):

    translation = ""
    for letter in phrase:
        if letter in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz":
                        translation = translation + letter + "o" + letter
        else:
            translation = translation + letter
    return translation


mytext = translate(input("skriv något: "))

language = 'sv'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("welcome.mp3")




print(mytext)