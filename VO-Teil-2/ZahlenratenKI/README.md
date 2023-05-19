# Zahlenraten (Binary Search)
(siehe dazu auch: https://www.inf-schule.de/imperative-programmierung/python/konzepte/ablaufmodellierung/beispiel_zahlenraten)

## Worum gehts? (Goal)
Du möchtest auf dem Discord-Server deiner Klasse einen Discord-Bot bereitstellen, mit dem man Zahlen-Raten-Spielen kann. Er soll möglichst "intelligent" Zahlen raten können.

## Deine Rolle? (Role)
Du bist an diesem Trick interessiert und möchtest herausfinden, wie *IAmLegend* das macht.

## Für wen? (Audience)
Du möchtest im Discord-Channel mit einem intelligenten Bot glänzen.

## Die Situation? (Situation)
Du überlegst dir, dass es hilfreich wäre, einen Discord-Bot in Python zu schreiben, der in möglichst wenigen Schritten eine durch die Benutzer ausgdachte Zufallszahl erraten kann. Die Benutzer denken sich eine Zahl aus und sagen dem Discord-Bot innerhalb welcher Unter- und Obergrenzen die Zahl liegt. Der Bot wird dann mit seinen Rateversuchen starten und mit möglichst wenigen Schritten zur Lösung kommen.

Du hast gehört, dass die binäre Suche in diesem Zusammenhang einen guten Ansatz für eine Lösung bieten könnte.

Bevor du den Bot aktivierst, möchtest du das Programm jedoch lokal bei dir in Python implementieren.

## Funktionale Anforderungen? (Product)
Für die Software gelten folgende funktionale Anforderungen:

- Der Bot nimmt die Unter- und die Obergrenze als Eingabe entgegen.
- Der Bot ratet die Zahlen anhand des Algorithmus "Binary Search".
  
## Die Bewertungsstandards? (Standards)
- Funktionalität der Software lt. Anforderungen
- Qualität des Codes
- Zeitmanagement
- ...

# Implementierung

## Blockbasierte Implementierung
![](./bilder/zahlenratenki1.png)
![](./bilder/zahlenratenki2.png)
![](./bilder/zahlenratenki3.png)
## Python-Implementierung KI-Variante (Binäre Suche)

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
        print("Zahl gefunden. Anzahl Versuche: " + str(anzahlVersuche))
        return
    elif feedback == "g":
        binaersuche_rekursiv(werte, mitte + 1, ende, anzahlVersuche+1)
    elif feedback == "k":
        binaersuche_rekursiv(werte, start, mitte - 1, anzahlVersuche+1)
def binaersucheKi(werte):
    binaersuche_rekursiv(werte, 0, len(werte) - 1, 1)
min = int(input("Minimum: "))
max = int(input("Maximum: "))
moeglicheWerte = list(range(min,max+1))
binaersucheKi(moeglicheWerte)
```

## Implementierung für Microbit (Microsoft MakeCode)
```python
def on_gesture_shake():
    global list2
    list2 = range(1, 101)
    binaersuche_rekursiv(list2, 0, len(list2) - 1, 1)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def binaersuche_rekursiv(werte: List[number], start: number, ende: number, anzahlVersuche: number):
    global mitte, feedback
    if ende < start:
        basic.show_icon(IconNames.NO)
        basic.pause(2000)
        control.reset()
    mitte = Math.idiv(start + ende, 2)
    basic.show_number(werte[mitte])
    while True:
        if input.button_is_pressed(Button.A):
            feedback = "k"
            break
        elif input.button_is_pressed(Button.B):
            feedback = "g"
            break
        elif input.logo_is_pressed():
            feedback = "r"
            break
    if feedback == "r":
        basic.show_icon(IconNames.HAPPY)
        basic.pause(2000)
        control.reset()
    elif feedback == "g":
        binaersuche_rekursiv(werte, mitte + 1, ende, anzahlVersuche + 1)
    elif feedback == "k":
        binaersuche_rekursiv(werte, start, mitte - 1, anzahlVersuche + 1)
feedback = ""
mitte = 0
list2: List[number] = []
```