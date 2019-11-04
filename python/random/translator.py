def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz":
                        translation = translation + letter + "o" + letter
        else:
            translation = translation + letter
    return translation



print(translate(input("Enter a phrase: ")))