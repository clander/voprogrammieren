import random
wortliste = ["Haus", "Garten", "Zaun", "Mensch", "Dampfschiff", "Katze", "Schule"]
zufallswort = wortliste[random.randint(0,len(wortliste)-1)]
ratewort = list("_" * len(zufallswort))
#print(zufallswort)
rateversuche = 0
fehlversuche = 0
maxfehlversuche = 10
wortErraten = False
zuvieleFehlversuche = False
while(not wortErraten and not zuvieleFehlversuche):
    print(ratewort)
    eingabe = input("Rate einen Buchstaben ... ")
    rateversuche = rateversuche + 1
    treffer = False 
    for index in range(0,len(zufallswort)):
        if ratewort[index] == "_" and eingabe == zufallswort[index]:
            ratewort[index] = zufallswort[index]
            treffer = True
    if treffer == False:
        fehlversuche = fehlversuche + 1
        if fehlversuche > maxfehlversuche:
            print("Du hast leider zuviele Fehlversuche! Spiel beendet!")
            zuvieleFehlversuche = True
    if ratewort.count("_")==0:
        print("Super! Du hast das Wort mit " + str(fehlversuche) +" Fehlversuch(en) erraten")
        wortErraten = True