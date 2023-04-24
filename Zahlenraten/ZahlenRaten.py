import random, sys
min = 1
max = 10
eingabeZahl = -1
anzahlVersuche = 0
zufallszahl = random.randrange(min,max)
gefunden = False
while not gefunden:    
    eingabe = input(f"Zahl zwischen {min} und {max} eingeben!")
    if eingabe.isnumeric():
        eingabeZahl = int(eingabe)
        if eingabeZahl == zufallszahl:
            anzahlVersuche = anzahlVersuche + 1
            print(f"Du hast die Zahl erraten! Anzahl der Versuche: {anzahlVersuche}")
            gefunden = True
        elif eingabeZahl < zufallszahl:
            print("Leider nicht, die gesucht Zahl ist größer!")
            anzahlVersuche += 1
        elif eingabeZahl > zufallszahl:
            print("Leider nicht, die gesucht Zahl ist kleiner!")
            anzahlVersuche += 1
print("Auf Wiedersehen!")
