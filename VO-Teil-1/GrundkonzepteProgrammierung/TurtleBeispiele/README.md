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
Die folgenden Beispiele können in https://blockpy.cis.udel.edu/ oder in https://app.edublocks.org/editor oder in jeder aktuellen anderen Python-Umgebung ausprobiert werden. 


# Regelmäßige Polygone mit Turtle-Grafik

## Problemstellung

### Ziel
Für die Volksschule Urgen soll eine Geometrie-App Namens POLYGONIX entwickelt werden, mit der Kinder geometrische Figuren kennenlernen können.
### Deine Rolle
Du bist Schüler:in im Fach Digitale Grundbildung.
### Zielgruppe
Die Zielgruppe für die App sind Volksschulkinder der 3. und 4. Klasse.
### Situation
Im Fach Digitale Grundbildung lernst du, wie man kleine Computerprogramme schreibt, mit denen man geometrische Figuren mittels Turtle-Grafik zeichnen kann. Nutze die erlangten Kompetenzen und hilf bei der Entwicklung der App.
### Produkt

Die App soll folgende Funktionen aufweisen:

1. STARTBILDSCHIRM: Nach dem Start der App, sollen die Kinder mit einem schönen Startbildschirm aus lauter geometrischen Figuren begrüßt werden.
2. LERNMODUS: Im Lernmodus der App sollen die Schüler:innen über eine Auswahl die Möglichkeit haben, verschiedene regelmäßige Polygone auf dem Bildschirm anzuzeigen (Quadrate, Dreiecke, Fünfecke etc.). Zusammen mit dem jeweiligen Polygon wird der Name des Polygons und die Anzahl der Ecken angezeigt. Damit die Schüler:innen sich beim Zählen leichter tun, soll jede zweite Seite eine andere Farbe aufweisen. Die Polygone sollen mit verschiedenen Farben ausgemalt werden.
3. ÜBUNGSMODUS: Im Übungsmodus der App bekommen die Schüler:innen ein zufälliges Polygon angezeigt, und sie müssen korrekt beantworten, um welche Art von Polygon es sich handelt.

## POLYGONIX 1.0

### Erwünschte Lösung (Spezifikation)
Für Version 1.0 der App POLYGONIX 1.0 soll der LERNMODUS implementiert werden.

Im Lernmodus der App sollen die Schüler:innen über eine Auswahl die Möglichkeit haben, verschiedene regelmäßige Polygone auf dem Bildschirm anzuzeigen (Quadrate, Dreiecke, Fünfecke etc.). Zusammen mit dem jeweiligen Polygon wird der Name des Polygons und die Anzahl der Ecken angezeigt.

### Eingabe - Verarbeitung - Ausgabe:
Die Schüler:innen starten die App.
Sofort werden sie aufgefordert, eine Anzahl von gewünschten Ecken einzugeben.

Die Eingabe muss eine positive Zahl größer gleich 3 sein.

Auf dem Bildschirm wird ein regelmäßiges Polygon ausgegeben, zusammen mit der Anzahl der Ecken.

### Abstraktion:
Wir benötigen als Eingabe lediglich eine Zahl, die wir uns für das Zeichnen des Polygons merken müssen.
Ein Polygon besteht aus Kanten mit einer bestimmten Seitenlänge, die in einem bestimmen Winkel zueinander stehen.

Mit Hilfe der Turtle-Grafik-Bibliothek können wir mit einem Zeichenstift (Turtle) Linien zeichnen, Farben für die Linien definieren, den Zeichenstift eine bestimmte Anzahl an Grad (Winkel) zu drehen und gezeichnete Figuren mit Farben ausfüllen.
### Generalisierung:
Es gilt folgende Regel: In einem regelmäßigen Polygon muss die Summe aller Winkel 360 Grad ergeben.

Für ein Dreieck (3 Seiten) zeichnen wir 3 Kanten, jeweils in einem Winkel von 360 : 3 = 180 Grad zueinander.
Für ein Quadrat (4 Seiten) zeichnen wir 4 Kanten, jeweils in einem Winkel von 360 : 4 = 90 Grad zueinander.
Für ein Fünfeck (5 Seiten) zeichnen wir 5 Kanten, jeweils in einem Winkel von 360 : 5 = 72 Grad zueinander.
Für ein Sechsecke (6 Seiten) zeichnen wir 6 Kanten, jeweils in einem Winkel von 360 : 6 = 60 Grad zueinander.

### Mustererkennung:
Die Grad in einem regelmäßigen Polygon sind also Abhänging von der Anzahl der Ecken. 

Die Anzahl der Ecken spielt außerdem auch eine wichtige Rolle, beim Zeichnen der Polygone.

Für ein Dreieck gehen wir wie folgt vor:
1. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 180 Grad
2. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 180 Grad
3. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 180 Grad

Für ein Viereck gehen wir wie folgt vor:
1. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 90 Grad
2. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 90 Grad
3. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 90 Grad
4. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 90 Grad

Für ein Fünfeck gehen wir wie folgt vor:
1. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 72 Grad
2. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 72 Grad
3. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 72 Grad
4. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 72 Grad
5. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 72 Grad

usw.

Ein weiteres Muster betrifft außerdem die Farbe. Laut Spezifikation müssen wir zumindest jede zwei aneinander grenzende Seiten in einer anderen Farbe ausgeben, also z.B.: 

1. Seite: Farbe Schwarz
2. Seite: Farbe Blau
3. Seite: Farbe Schwarz
4. Seite: Farbe Blau
5. ...

## Algorithmisierung

### POLYGONIX VERSION 0.1 (Dreieck)

```python
Wir definieren die Linienfarbe "black"
Wir zeichnen eine Linie der Länge 100
Wir drehen uns um 180 Grad
Wir definieren die Linienfarbe "blue"
Wir zeichnen eine Linie der Länge 100
Wir drehen uns um 180 Grad
Wir definieren die Linienfarbe "black"
Wir zeichnen eine Linie der Länge 100
Wir drehen uns um 180 Grad
```

```mermaid


```

### POLYGONIX VERSION 0.2

```python
Wir fragen den Benutzer nach der Anzahl der Ecken und merken uns die Zahl
Wenn der Benutzer 3 eingegeben hat:
    Wir definieren die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 180 Grad
    Wir definieren die Linienfarbe "blue"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 180 Grad
    Wir definieren die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 180 Grad
Wenn der Benutzer 4 eingegeben hat:
    Wir definieren die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 90 Grad
    Wir definieren die Linienfarbe "blue"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 90 Grad
    Wir definieren die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 90 Grad
    Wir definieren die Linienfarbe "blue"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 90 Grad
Wenn der Benutze weder 3 noch 4 eingegeben hat
    Wir geben eine Information aus, dass das noch nicht unterstützt wird.
```

### POLYGONIX VERSION 0.3

```python
Wir fragen den Benutzer nach der Anzahl der Ecken und merken uns die Zahl.
Wir definieren die Linienfarbe "black"
Wir definieren einen Zähler mit dem Startwert 0, der die Anzahl der Wiederholungen enthält.
Wir wiederholen solange der Zähler kleiner als die eingegebene Anzahl von Ecken ist:
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um (360 : anzahl_ecken) Grad
    Wir zählen den Zähler um 1 hoch.
```

### POLYGONIX VERSION 0.4

```python
Wir fragen den Benutzer nach der Anzahl der Ecken und merken uns die Zahl.
Wir definieren einen Zähler mit dem Startwert 0, der die Anzahl der Wiederholungen enthält.
Wir wiederholen solange der Zähler kleiner als die eingegebene Anzahl von Ecken ist:
    Wenn der Zähler durch 2 teilbar ist:
        Wir setzen die Linienfarbe "blue"
    Ansonsten:
        Wir setzen die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um (360 : anzahl_ecken) Grad
    Wir zählen den Zähler um 1 hoch.
```

### POLYGONIX VERSION 0.5

```python
Wir fragen den Benutzer nach der Anzahl der Ecken und merken uns die Zahl.
Wir definieren einen Zähler mit dem Startwert 0, der die Anzahl der Wiederholungen enthält.
Wir wiederholen solange der Zähler kleiner als die eingegebene Anzahl von Ecken ist:
    Wenn der Zähler durch 2 teilbar ist:
        Wir setzen die Linienfarbe "blue"
    Ansonsten:
        Wir setzen die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um (360 : anzahl_ecken) Grad
    Wir zählen den Zähler um 1 hoch.
```

### POLYGONIX VERSION 1.0

```python
Wir fragen den Benutzer nach der Anzahl der Ecken und merken uns die Zahl.
Solange die Zahl keine Zahl größer oder gleich 3 ist:
    Der Benutzer bekommt einen Hinweis, dass nur Zahlen ab 3 erlaubt sind.
    Der Benutzer muss die Zahl erneut eingeben.
Wir definieren einen Zähler mit dem Startwert 0, der die Anzahl der Wiederholungen enthält.
Wir wiederholen solange der Zähler kleiner als die eingegebene Anzahl von Ecken ist:
    Wenn der Zähler durch 2 teilbar ist:
        Wir setzen die Linienfarbe "blue"
    Ansonsten:
        Wir setzen die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um (360 : anzahl_ecken) Grad
    Wir zählen den Zähler um 1 hoch.
```


  
## Implementierung und Test
Nachdem wir unseren Lösungsalgorithmus geplant haben, gehen wir in die Umsetzung über. Dazu suchen wir ein Werkzeug, das es uns aufgrund der unterstützten Konzepte bzw. aufgrund des gewählten Modellierungsparadigmas ermöglicht, den Algorithmus umzusetzen, auszuführen und zu testen. 

Die Implementierung wird immer wieder ausgeführt, getestet und modifiziert, solange bis die Lösung fertig ist. Im Rahmen der Modifikation kann / wird es zu Anpassungen des Lösungsansatzes sowie des Algorithmus kommen, was zu weiteren Zyklen führt. Die Lösung soll außerdem so weit wie möglich generalisiert werden, d.h. sie soll eine Klasse von Problemen und nicht nur ein spezifisches Problem mit bestimmten spezifischen Daten lösen.

Der Ablauf lässt sich also wie folgt kurz beschreiben:

* Wir beginnen mit der Implementierung des Programms mithilfe des gewählten Werkzeugs (bestimmte Programmiersprache, bestimmte Entwicklungsumgebung). 
* In kurzen Zyklen werden wir nach jeder kurzen Programmiertätigkeit immer wieder das Programm versuchen auszuführen. 
* Wenn sich das Programm nicht starten lässt, analysieren wir die Fehlermeldungen des Compilers und bessern Syntaxfehler aus. Wir müssen uns an die Syntax der gewählten Programmiersprache ganz genau halten, sonst versteht der Computer nicht, was er für uns tun soll. 
* Wenn sich das Programm jedoch starten lässt, können wir kontrollieren, ob das Programm die richtigen (Teil-)Ergebnisse im Sinne unserer Lösungsspezifikation liefert. Dazu benötigen wir Techniken, die es uns ermöglichen in die Laufzeit eines Programmes hineinzuschauen bzw. Ergebnisse des Programmes anzuzeigen (Debugging-Strategien). 
* Falls das Programm beim Ausführen noch keine korrekten Lösungen / Lösungsteile liefert, haben wir es ggf. mit einem Bug zu tun, die Semantik passt also nicht. 
* Dann können Modifikation in der Problemanalyse, im Algorithmus oder auch im Code nötig werden (zyklische Natur). Eine Modifikation der Problemanalyse führt zu Modifikation des Algorithmus und der Implementierung. 
* Eine Modifikation im Algorithmus führt zu einer Modifikation der Implementierung. Jedenfalls wird es also immer Modifikationen in der Implementierung brauchen, um den Bug zu beheben.
* Wenn das Programm im Sinne Lösungsspezifikation korrekte Ergebnisse liefert, dann sind wir fertig. Handelt es sich nur um eine Teillösung, gehen wir zur Bearbeitung des nächsten Lösungsteils über. Ggf. müssen gegen Ende mehrere Lösungsteile miteinander verbunden werden, um zur Gesamtlösung zu kommen.








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