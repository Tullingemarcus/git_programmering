
def translate(string):
    translation = ""
    for phrase in string:
        if phrase in "tot":
                translation = "t";
    for phrase in string:       
        if phrase in "lol":
                transalation = "l";
        else:
            translation = string
    return translation




print(translate(input("Enter a phrase: ")))