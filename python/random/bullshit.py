grader = {"timmar: ": , "minuter": , "sekunder:": }

def main ():
    convert = input("vad vill du konverta: ")
    if convert == "x":
        krokodil()

    elif convert == "y":
        klocka()
    else:
        print()



def krokodil():
    meter = float(input("skriv in hur många meter: "))
    krokodiler = meter/4.2
    print(krokodiler)

def pingvin():
    vikt = float(input("hur mycket vikt: "))
    pingviner = vikt/2.5
    print(pingviner)

def klocka():
    for h in grader:
        q = input(h[0)
        h.append(q)
        grader[0] = float(h[1])*30
        grader[1] = float(h[1])*6
        grader[2] = float(h[1])*6
    print("klockan är", timgrad, "timgrader ", mingrad, "minutgrader och ", secgrad, "sekundgrader")


if __name__ == "__main__":
    main()