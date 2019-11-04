VOWELS = 'AEIOUYÅÄÖ'


def main() -> None:
    word = input('Enter Phrase : ')
    final_word = rövarspråket(word)
    print(final_word)


def is_vowel(letter: str) -> bool:
    return letter.upper() in VOWELS


def rövarspråket(word: str) -> str:
    translation = ""
    for letter in word:
        if letter in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz":
                        translation = translation + letter + "o" + letter
        else:
            translation = translation + letter
    return translation


def decode_rövarspråket(word: str) -> str:
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