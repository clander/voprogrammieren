import random

min = 1
max = 10
print("Raten Sie eine Zahl zwischen {0:d} und {1:d}".format(min,max))

eingabeZahl = -1
anzahlVersuche = 0
zufallszahl = random.randrange(min,max)

while True:    
    eingabe = input("Zahl zwischen {0:d} und {1:d} eingeben!".format(min,max))
    if not eingabe.isnumeric():
        continue
    eingabeZahl = int(eingabe)
    if eingabeZahl == zufallszahl:
        print("Du hast die Zahl erraten! Anzahl der Versuche: {0:d}".format(anzahlVersuche))
        break
    elif eingabeZahl < zufallszahl:
        print("Leider nicht, die gesucht Zahl ist größer!")
        anzahlVersuche += 1
    elif eingabeZahl > zufallszahl:
        print("Leider nicht, die gesucht Zahl ist kleiner!")
        anzahlVersuche += 1