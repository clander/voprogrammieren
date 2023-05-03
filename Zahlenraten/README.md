# Zahlenraten

## Worum gehts? (Goal)
Auf dem Discord-Server deiner Klasse hat der User IAmLegend behauptet, dass er es schafft, jede ausgedachte Zahl innerhalb des Zahlenraumes 1 bis 100 in maximal 7 Versuchen zu erraten. 

## Deine Rolle? (Role)
Du bist an diesem Trick interessiert und möchtest herausfinden, wie IAmLegend das macht.

## Für wen? (Audience)
Du möchtest im Discord-Channel mit der Auflösung des Tricks glänzen.
## Die Situation? (Situation)
Du überlegst dir, dass es hilfreich wäre, einen Discord-Bot in Python zu schreiben, der sich zufällig eine Zahl ausdenkt und dann die Benutzer im Channel nach der Zahl fragt. Du gibst die Zahl ein und bekommst vom Bot dann den Hinweis, ob die gesucht Zahl kleiner, größer oder korrekt ist. Damit kannst du und deine Kollegen trainieren und prüfen, mit welcher Strategie du ebenfalls in maximal 7 Versuchen zur Lösung kommen kannst.

Außerdem könnt ihr damit prüfen, ob IAmLegend den Trick wirklich beherrscht.

Bevor du den Bot aktivierst, möchtest du das Programm jedoch lokal bei dir in Python implementieren.

## Funktionale Anforderungen? (Product)
Für die Software gelten folgende funktionale Anforderungen:
- Das Programm denkt sich eine zufällige Zahl zwischen 1 und 100 aus.
- Das Programm fragt dich nach der korrekten Zahl.
- Das Programm gibt den Hinweis "Kleiner" oder "Größer" aus, wenn du die Zahl nicht erraten hast.
- Das Programm gibt die Anzahl der Versuche aus, wenn du die Zahl erraten hast.
- ...
- 
## Funktionale Anforderungen Discord-Bot-KI
In einer erweiterten Version der Software könnte man einen Discord-Bot implementieren, der in einem zweiten Modus eine von den Usern des Discord-Channels ausgedachte Zahl zwischen 1 und 100 mit maximal 7 Versuchen finden kann ... eine kleine KI sozusagen.
## Die Bewertungsstandards? (Standards)
- Funktionalität der Software lt. Anforderungen
- Qualität des Codes
- Zeitmanagement
- ...

# Implementierungen
## Blockbasierte Implementierung Basisvariante

![](/Zahlenraten/bilder/zahlenraten1.png)
![](/Zahlenraten/bilder/zahlenraten2.png)
## Python-Implementierung Basisvariante
```python
import random
min = 1
max = 100
anzahlVersuche = 0
zufallszahl = random.randint(min, max)
gefunden = False
while not gefunden:
    eingabe = input("Zahl zwischen " + str(min) + " und " + str(max) + " eingeben!")
    if eingabe.isnumeric():
        eingabeZahl = int(eingabe)
        if eingabeZahl == zufallszahl:
            anzahlVersuche = anzahlVersuche + 1
            print("Du hast die Zahl erraten! Anzahl der Versuche:" + str(anzahlVersuche))
            gefunden = True
        elif eingabeZahl < zufallszahl:
            print('Leider nicht, die gesucht Zahl ist größer!')
            anzahlVersuche += 1
        else:
            print('Leider nicht, die gesucht Zahl ist kleiner!')
            anzahlVersuche += 1
print('Auf Wiedersehen!')
```

## Blockbasierte Implementierung KI-Variante
![](/Zahlenraten/bilder/zahlenratenki1.png)
![](/Zahlenraten/bilder/zahlenratenki2.png)
![](/Zahlenraten/bilder/zahlenratenki3.png)
## Python-Implementierung KI-Variante

```python
def binaersuche_rekursiv(werte, start, ende, anzahlVersuche):
    if ende < start:
        print('Ich kann deine Zahl nicht gefunden! Ich glaube du schwindelst!')
        return
    mitte = (start + ende) // 2
    print("Ich rate ... " + str(werte[mitte])) 
    feedback = ""
    while feedback not in ("r","k","g"):
        feedback = input("(r)ichtig (k)leiner oder (g)rößer? ")
    if feedback == "r":
        print("Zahl gefunden. Anzahl versuche: " + str(anzahlVersuche))
        return
    elif feedback == "g":
        return binaersuche_rekursiv(werte, mitte + 1, ende, anzahlVersuche+1)
    elif feedback == "k":
        return binaersuche_rekursiv(werte, start, mitte - 1, anzahlVersuche+1)
def binaersucheKi(werte):
    return binaersuche_rekursiv(werte, 0, len(werte) - 1, 1)
min = int(input("Minimum: "))
max = int(input("Maximum: "))
moeglicheWerte = list(range(min,max+1))
binaersucheKi(moeglicheWerte)

```

