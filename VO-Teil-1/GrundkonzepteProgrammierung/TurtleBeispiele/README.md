# Miniwelten und Turtle-Grafik

## Steuerung von Akteuren in Miniwelten (Überblick)
Die Steuerung von Akteuren in Miniwelten ist eine beliebte Form des einführenden Programmmierunterrichts. Die Lernenden definieren Algorithmen zur Steuerung der Akteure und lösen damit die definierten Aufgaben.

Beispielwerkzeuge dafür sind:

- Turtle-Grafik (Logo, in verschiedenen Versionen)
- Roboter Karol: 
  - https://karol.arrrg.de (online)
  - http://cgd.zum.de/wiki/Programmieren_lernen_mit_Robot_Karol
- Kara Marienkäfer: https://www.swisseduc.ch/informatik/karatojava/kara/
- Hamster-Modell: http://www.java-hamster-modell.de/index2.html
- Open Roberta Sim (Robotersimulation): https://www.open-roberta.org
- Scratch (Multimedia- und Spieleprogrammierung): https://scratch.mit.edu
- Snap! (Großer Bruder von Scratch) https://snap.berkeley.edu
- Swift Playgrounds (Programmieren lernen im Apple-Ökosystem): https://www.apple.com/de/swift/playgrounds/ 
- Multimedia-Art mit Processing (https://processing.org)
- Pen and Paper Varianten wie hier beschrieben: 
  - https://microbit.eeducation.at/wiki/Hauptseite, Version 2, S. 11 bis S. 18

Weitere Vertreter: https://de.wikipedia.org/wiki/Bildungsorientierte_Programmiersprache

## Beispiele mit Roboter Karol

- Siehe Tutorial in der entsprechenden Online-Umgebung: https://karol.arrrg.de

## Beispiele mit LOGO (in Python)

### Einführung
Logo ist die älteste Form der Realisierung des Miniwelt-Konzepts für die einführende Programmierung. Logo wurde von Seymour Papert in den 60er Jahren entwickelt und ist über die Jahre in immer wieder neuen Varianten herausgekommen. In Logo wird eine Schildkröte die zeichnen kann (Turtle) auf einer Zeichenfläche bewegt (Turtle-Grafik). Die Steuerung der Schildkröte erfolgt über eine Programmiersprache. Programmieraufgaben in Logo betreffen meist die Produktion von geometrischen Figuren (Turtle-Grafik).

Die Logo-Turtle lässt sich in jeder Python-Standarddistribution (und auf entsprechenden Plattformen auch blockbasiert) programmieren. Es gibt aber auch unzählige andere Varianten. 

Hintergrund: https://de.wikipedia.org/wiki/Logo_%28Programmiersprache%29

Viele der später aufgekommenen Miniwelten (Kara, Karol, Scratch etc.) basieren auf dem Konzept der Miniwelt.

### Beispiele für den Einstieg
Die folgenden Beispiele können in https://blockpy.cis.udel.edu/ oder in https://app.edublocks.org/editor oder in jeder anderen Python-Umgebung ausprobiert werden. 

**Quadrat** mit verschiedenen Seitenfarben (einfach)

```python
import turtle
turtle.pensize(5)
turtle.forward(40)
turtle.right(90)
turtle.pencolor("red")
turtle.forward(40)
turtle.right(90)
turtle.pencolor("green")
turtle.forward(40)
turtle.right(90)
turtle.pencolor("blue")
turtle.forward(40)
turtle.right(90)
```

**Quadrat**

```python
import turtle
seitenlaenge = int(input('Seitenlänge?'))
i=0
while i < 4:
    turtle.forward(seitenlaenge)
    turtle.right(90)
    i = i + 1
```

**Vieleck**

```python
import turtle
ecken = int(input("Wieviele Ecken?"))
seitenlaenge = int(input("Seitenlänge?"))
i = 0
while i < ecken:
    turtle.forward(seitenlaenge)
    turtle.right(360/ecken)
    i = i +1
```

**Vieleck mit zwei Farben**

```python
import turtle
ecken = int(input("Wieviele Ecken?"))
seitenlaenge = int(input("Seitenlänge?"))
stiftdicke = int(input("Wie dick sollen die Linien sein?"))
turtle.pensize(stiftdicke)
i = 0
while i < ecken:
    if i % 2 == 0:
        farbe = "red"
    else:
        farbe = "black"
    turtle.pencolor(farbe)
    turtle.forward(seitenlaenge)
    turtle.right(360/ecken)
    i = i +1
```
**Vieleck mit verschiedenen, zufälligen Farben** (Array-Random-Variante)

```python
import turtle, random
ecken = int(input('Wieviele Ecken?'))
seitenlaenge = int(input('Seitenlänge?'))
farben = ['blue', 'red', 'green', 'yellow', 'black']
i = 0
while i < ecken:
    zufallFarbe = farben[random.randint(0, 4)]
    turtle.pencolor(zufallFarbe)
    turtle.forward(seitenlaenge)
    turtle.right(360 / ecken)
    i = i + 1
```
**Spirale**

```python
import turtle
seitenlaenge = 10
while seitenlaenge < 100:
    seiten = 2
    while seiten > 0:
        turtle.forward(seitenlaenge)
        turtle.right(90)
        seiten = seiten - 1
    seitenlaenge = seitenlaenge + 5
```

**Fibonacci-Quadrate**

```python
import turtle
schritteAnzahl = 13
nMinus2 = 0
nMinus1 = 1
while schritteAnzahl > 0:
    schritteAnzahl = schritteAnzahl - 1
    n = nMinus2 + nMinus1
    i = 0
    while i < 4:
        turtle.forward(n)
        turtle.right(90)
        i = i + 1
    nMinus2 = nMinus1
    nMinus1 = n
```