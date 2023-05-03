# Schere-Stein-Papier
Schere-Stein-Papier ist zwar retro aber lustig. Du möchtest dieses Spiel in Python programmieren und später als Discord-Bot bereitstellen.

Für die Software gelten folgende funktionale Anforderungen:

Der Benutzer / die Benutzerin möchte gegen das Programm ein Schere-Stein-Papier Match spielen können.

  - Version 1: Das Programm wählt einfach nur zufällig Schere, Stein oder Papier und zeigt das Ergebnis an. Der Benutzer denkt sich selbst Schere, Stein und Papier aus und legt selbst fest, ober er/sie gewonnen oder verloren hat. 
  - Version 2: Das Programm wählte zufällig Schere, Stein, Papier aus, lässt den Benutzer seine Wahl eingeben und entscheidet, wer gewonnen hat. 
  - Version 3: Das Programm soll am Ende eine Statistik mit den Spieler- bzw. Programmgewinnen anzeigen und es soll ausgeben, wer das Match insgesamt gewonnen hat.

# Implementierungen

## Blockbasierte Implementierung
![](/SchereSteinPapier/bilder/ssp1.png)
![](/SchereSteinPapier/bilder/ssp2.png)
![](/SchereSteinPapier/bilder/ssp3.png)
![](/SchereSteinPapier/bilder/ssp4.png)
![](/SchereSteinPapier/bilder/ssp5.png)

## Python-Implementierung

```python
import random
print("*** Schere, Stein, Papier ***")
spielerGewinne = 0
computerGewinne = 0
while True:
    spielerwahl = input("Was wählst du? Tippe ein: [Schere]  [Stein]  [Papier]  [Exit] ")
    if spielerwahl != "Schere" and spielerwahl != "Stein" and spielerwahl != "Papier" and spielerwahl != "Exit":
        print("Es stehen nur folgende Optionen zur Verfügung: [Schere]  [Stein]  [Papier]  [Exit] ")
        continue
    elif spielerwahl == "Exit":
        break
    else:
        zufallszahl = random.randint(0,2)
        if zufallszahl == 0:
            computerwahl = "Schere"
        elif zufallszahl == 1:
            computerwahl = "Stein"
        elif zufallszahl == 2:
            computerwahl = "Papier"
        print("[Spielerwahl] : " + spielerwahl)
        print("[Computerwahl] : " + computerwahl)
        if spielerwahl == computerwahl:
            print(">Unentschieden")
        elif spielerwahl == "Schere" and computerwahl == "Papier":
            print(">Spieler gewinnt")
            spielerGewinne = spielerGewinne + 1
        elif spielerwahl == "Stein" and computerwahl == "Schere":
            print(">Spieler gewinnt")
            spielerGewinne = spielerGewinne + 1
        elif spielerwahl == "Papier" and computerwahl == "Stein":
            print(">Spieler gewinnt")
            spielerGewinne = spielerGewinne + 1
        else:
            print(">Computer gewinnt")
            computerGewinne = computerGewinne + 1
print("")
print("*************** Statistik ***************")
print(str(spielerGewinne) + " (Spieler) : " + str(computerGewinne) + " (Computer)")
if spielerGewinne > computerGewinne:
    print("Spieler gewinnt das Match")
elif computerGewinne > spielerGewinne:
    print("Computer gewinnt das Match")
else:
    print("Das Match geht untentschieden aus!")
print("*****************************************")

```

