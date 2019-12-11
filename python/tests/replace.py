


def replace():
    phrase = word()
    output = ""
    for letter in phrase:
        if letter in "(),":
                        phrase = phrase + letter.replace(letter, "")
        else:
            output = output + letter
    return output

def word():
    return "(hallå där),"

print(replace())
