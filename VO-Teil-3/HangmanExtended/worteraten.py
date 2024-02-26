from pathlib import Path
import random

def wortliste_laden(dateiname:str):
    path = Path(__file__).with_name(dateiname)
    with path.open(mode='r',encoding='utf-8') as file:
        wortliste = file.read().splitlines()
        return wortliste 

def hinweis(hinweis_ratewort:list,hinweis_zufallswort:str):
    for index in range(0,len(hinweis_zufallswort)):
        if hinweis_ratewort[index] == "_":
            print(zufallswort[index])
            return

def fehlerbalken_ausgeben(maximum:int, fuellstand:int):
    if fuellstand > maximum:
        fuellstand = maximum
       
    print('[', end="")
    
    for _ in range(fuellstand):
        print('x', end="")
    
    for _ in range(maximum-fuellstand):
        print('_', end="")
    
    print(']')
    

worteliste = wortliste_laden("nomen.txt")
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
                print(f"Ups. Falsch. Du hast noch {max_fehlversuche-fehlversuche} Fehlversuch(e) ... ", end="")
                fehlerbalken_ausgeben(max_fehlversuche,fehlversuche)

if(wort_erraten and not zuviele_fehlversuche):
    print("".join(ratewort))
    print("""
     Du hast das gesuchte Wort erraten!
     __*_____*________ 
    |  ____*___*____  |
    | | GRATULATION | |
    | |_*___________| |
    |_____*___*_______|
    """)
else:
    print("-------------------------------------------------------")
    print("Zuviele Fehlversuche! Spiel leider verloren 8-(")
    print("Das gesuchte Wort: "+ zufallswort)
    print("-------------------------------------------------------")