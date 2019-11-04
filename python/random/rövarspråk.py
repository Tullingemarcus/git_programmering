from gtts import gTTS

import os

VOWELS = 'AEIOUYÅÄÖ'

#första listan för första frågan
question = [("vilket håll vill du översätta: \n för svenska till rövarspråk skriv -1- \n för rövarspråk till svenska skriv -2- \n : ", "1", "2")]

#andra listan för andra frågan
question2 = [("vill du ha översättningen uppläst \n -ja- \n -nej- \n: ", "ja", "nej")]

#här får man välja vilket språk man vill översätta till samt vad man vill översätta
def main() -> None:
    for q in question:
        anwser = input(q[0])
        if (anwser.lower() == q[1]):
            word = input("sätt in något här: ")
            final_word = code_pirate(word)
            ask_tts(final_word)
        elif (anwser.lower() == q[2]):
            word = input("sätt in något här: ")
            final_word = decode_pirate(word)
            ask_tts(final_word)
        else:
            print("404 error")
            final_word = ""
    return final_word

def is_vowel(letter: str) -> bool:
    return letter.upper() in VOWELS

#fixar text to speech
def ask_tts(tts_text):
    for q2 in question2:
        svar = input(q2[0])
        if (svar.lower() == q2[1]):
            language = 'sv'
            myobj = gTTS(text=tts_text, lang=language, slow=False)
            myobj.save("welcome.mp3")
            os.system("welcome.mp3")
            print(tts_text)
        elif (svar.lower() == q2[2]):
            print(tts_text)
        else:
            print("404 error")

#krypterar till rövarspråk
def code_pirate(word: str) -> str:
    translation = ""
    for letter in word:
        if letter in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz":
                        translation = translation + letter + "o" + letter
        else:
            translation = translation + letter
    return translation

#dekrypterar från rövarspråk
def decode_pirate(word: str) -> str:
    original_word = []
    i = 0
    while i <= (len(word) - 1):
        character = word[i]
        original_word.append(character)
        if character.isalpha() and not is_vowel(character):
            i += 3
        else:
            i += 1
    return ''.join(original_word)

if __name__ == "__main__":
  main()