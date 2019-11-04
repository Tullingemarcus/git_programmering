#välkommen till mitt quiz

score = 0

#listan för både frågor och svar
quiz = [('\nvilket är världens näst största land: ', 'kanada'),
        ('\nvilket språk pratar man i österrike: \n A.tyska \n B.svenska \n C.engelska \n:', 'a'),
        ('\nvilket år startade andra världskriget: ', '1939'),
        ('\nvilket år bytte sverige till högertrafik: ', '1967'),
        ('\nvem var den andra personen på månen: ', 'buzz aldrin')]

#loopen som gör så allt funkar
for q in quiz:
    anwser = input(q[0])
    if (anwser.lower() == q[1]):
        score = score + 1
        print('-rätt-')
    else:
        print('-fel-')
        print("rätt svar var: ", q[1])

#printar ut scoret
print("du hade", score * 100 / len(quiz), "% ", "rätt")