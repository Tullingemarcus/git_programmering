anwser1 = "kanada"
anwser2 = "A"
anwser4 = "1967"
anwser5 = "buzz aldrin"
lost = "fel svar"
win = "rätt svar"

quiz1 = input("vilket är världens näst största land: ")
if (quiz1.lower() == anwser1):
    print(win)
    quiz1 = 1
else:
    print(lost)
    quiz1 = 0
    
quiz2 = input("vilket språk pratar man i österrike: A.tyska B.svenska C.engelska: ")
if quiz2 == anwser2.lower():
    print(win)
    quiz2 = 1
    
else:
    print(lost)
    quiz2 = 0

quiz3 = input("vilket år startade andra världskriget: ")
if (quiz3.lower() == "1939"):
    print(win)
    quiz3 = 1
    
else:
    print(lost)
    quiz3 = 0

quiz4 = input("vilket år bytte sverige till högertrafik: ")
if (quiz4.lower() == anwser4):
    print(win)
    quiz4 = 1
    
else:
    print(lost)
    quiz4 = 0

quiz5 = input("vem var den andra personen på månen: ")
if (quiz5.lower() == anwser5):
    print(win)
    quiz5 = 1
    
else:
    print(lost)
    quiz5 = 0

point = quiz1 + quiz2 + quiz3 + quiz4 + quiz5 

procent = point/5*100

print("du hade", procent, "%", "rätt")