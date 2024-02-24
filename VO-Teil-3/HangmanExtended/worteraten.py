from pathlib import Path
import random

def wortliste_laden(path:str):
    path = Path(__file__).with_name('nomen.txt')
    with path.open(mode='r',encoding='utf-8') as file:
        wortliste = file.read().splitlines()
        return wortliste 

def hinweis(ratewort:list,zufallswort:str):
    for index in range(0,len(zufallswort)):
       if ratewort[index] == "_":
           print(zufallswort[index])
           return

worteliste = wortliste_laden("nouns.txt")
zufallswort = random.choice(worteliste)
ratewort = list("_"*len(zufallswort))
print("Hinweis: " + zufallswort)
fehlversuche = 0
max_fehlversuche = 10
wort_erraten = False
zuviele_fehlversuche = False

while not wort_erraten and not zuviele_fehlversuche:
    print(ratewort)
    eingabe = input("Rate einen Buchstaben ...")
    if(eingabe.lower()=="hinweis"):
        hinweis(ratewort,zufallswort)
        fehlversuche = fehlversuche + 2
    else:
        treffer = False
        for index in range(0,len(zufallswort)):
            if ratewort[index] == "_" and eingabe.lower() == zufallswort[index].lower():
                ratewort[index] = zufallswort[index]
                treffer = True
        if treffer:
            print("Treffer!")
            if ratewort.count("_")==0:
                wort_erraten = True
        else:
            fehlversuche = fehlversuche + 1
            if fehlversuche == max_fehlversuche:
                zuviele_fehlversuche = True
            else:
                print(f"Ups. Falsch. Du hast noch {max_fehlversuche-fehlversuche} Fehlversuch(e) ...")

if(wort_erraten and not zuviele_fehlversuche):
    print(ratewort)
    print("""
    __*_______*___ 
    |  ____*___*_  |
    | | Gewonnen | |
    | |_*________| |
    |_____*___*____|
    """)
else:
    print("-------------------------------------------------------")
    print("Zuviele Fehlversuche! Spiel leider verloren 8-(")
    print("-------------------------------------------------------")