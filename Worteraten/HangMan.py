import random, sys

wortliste = ["Haus", "Garten", "Zaun", "Mensch", "Dampfschiff", "Katze", "Schule"]
zufallswort = wortliste[random.randint(0,len(wortliste)-1)]
ratewort = list("_" * len(zufallswort))
#print(zufallswort)
rateversuche = 0
fehlversuche = 0
maxfehlversuche = 10

while(True):
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
        if fehlversuche == maxfehlversuche:
            print("Du hast leider zuviele Fehlversuche! Spiel beendet!")
            break
    if ratewort.count("_")==0:
        print(f"Super! Du hast das Wort mit {fehlversuche} Fehlversuch(en) erraten")
        break
    if rateversuche > 10:
        print("Du hast das Wort nicht erraten. Zuviele Versuche!")
        sys.exit()