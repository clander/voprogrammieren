# Zahlenraten

## Worum gehts? (Goal)
Auf dem Discord-Server deiner Klasse hat der User IAmLegend behauptet, dass er es schafft, innerhalb des Zahlenraumes 1 bis 100 eine Zahl in immer maximal 7 Versuchen zu erraten. 

## Deine Rolle? (Role)
Du bist an diesem Trick interessiert und möchtest herausfinden, wie IAmLegend das macht.

## Für wen? (Audience)
Du möchtest im Discord-Channel mit der Auflösung des Tricks glänzen.

## Die Situation? (Situation)
Du überlegst dir, dass es hilfreich wäre, ein kleines Computerprogramm zu schreiben, das sich zufällig eine Zahl ausdenkt und dich dann nach der Zahl fragt. Du gibst die Zahl ein und bekommst vom Programm dann den Hinweis, ob die gesucht Zahl kleiner, größer oder korrekt ist. Damit kannst du trainieren und prüfen, mit welcher Strategie du ebenfalls in maximal 7 Versuchen zur Lösung kommen kannst.

## Funktionale Anforderungen? (Product)
Für die Software gelten folgende funktionale Anforderungen:
### Gratis-Version der Software:
- Das Programm denkt sich eine zufällige Zahl zwischen 1 und 100 aus.
- Das Programm fragt dich nach der korrekten Zahl.
- Das Programm gibt den Hinweis "Kleiner" oder "Größer" aus, wenn du die Zahl nicht erraten hast.
- Das Programm gibt die Anzahl der Versuche aus, wenn du die Zahl erraten hast.
- ...
## Die Bewertungsstandards? (Standards)
- Funktionalität der Software lt. Anforderungen
- Qualität des Codes
- Zeitmanagement
- ...

## Blockbasierte Implementierung:

![](/Zahlenraten/bilder/zahlenraten1.png)
![](/Zahlenraten/bilder/zahlenraten2.png)
## Python-Implementierung
```python
import random
min = 1
max = 100
anzahlVersuche = 0
zufallszahl = random.randint(min, max)
gefunden = False
while not gefunden:
    eingabe = input("Zahl zwischen" + str(min) + " und " + str(max) + " eingeben!")
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