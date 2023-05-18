# POLYGONIX (Version 1.0 - Lernmodus)

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

Für ein Dreieck (3 Seiten) zeichnen wir 3 Kanten, jeweils in einem Winkel von 360 : 3 = 120 Grad zueinander.
Für ein Quadrat (4 Seiten) zeichnen wir 4 Kanten, jeweils in einem Winkel von 360 : 4 = 90 Grad zueinander.
Für ein Fünfeck (5 Seiten) zeichnen wir 5 Kanten, jeweils in einem Winkel von 360 : 5 = 72 Grad zueinander.
Für ein Sechsecke (6 Seiten) zeichnen wir 6 Kanten, jeweils in einem Winkel von 360 : 6 = 60 Grad zueinander.

### Mustererkennung:
Die Grad in einem regelmäßigen Polygon sind also Abhänging von der Anzahl der Ecken. 

Die Anzahl der Ecken spielt außerdem auch eine wichtige Rolle, beim Zeichnen der Polygone.

Für ein Dreieck gehen wir wie folgt vor:
1. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 120 Grad
2. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 120 Grad
3. Wir zeichnen eine Linie in einer bestimmten Farbe
   Wir drehen uns um 120 Grad

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

## POLYGONIX Version 0.1

### Algorithmisierung

#### Pseudoce
```python
Wir definieren die Linienfarbe "black"
Wir zeichnen eine Linie der Länge 100
Wir drehen uns um 120 Grad
Wir definieren die Linienfarbe "blue"
Wir zeichnen eine Linie der Länge 100
Wir drehen uns um 120 Grad
Wir definieren die Linienfarbe "black"
Wir zeichnen eine Linie der Länge 100
Wir drehen uns um 120 Grad
```
#### Struktogramm
![](bilder/polygonix_0_1.png)

### Implementierung

#### Blöcke
![](bilder/polygonix_blocks_0_1.png)
#### Python-Code
```python
import turtle
turtle.pensize(4)
turtle.fillcolor('yellow')
turtle.pencolor('black')
turtle.forward(100)
turtle.right(120)
turtle.pencolor('blue')
turtle.forward(100)
turtle.right(120)
turtle.pencolor('black')
turtle.forward(100)
turtle.right(120)
```

## POLYGONIX Version 0.1
### Algorithmisierung

#### Pseudocode
```python
Wir fragen den Benutzer nach der Anzahl der Ecken, konvertieren die Texteingabe in eine Zahl und merken uns die Zahl.
Wenn der Benutzer 3 eingegeben hat:
    Wir definieren die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 120 Grad
    Wir definieren die Linienfarbe "blue"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 120 Grad
    Wir definieren die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um 120 Grad
Sonst:
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
    Sonst:
        Wir geben eine Information aus, dass das noch nicht unterstützt wird.
```
#### Struktogramm
![](bilder/polygonix_0_2.png)

### Implementierung

#### Blöcke 
![](bilder/polygonix_blocks_0_2_1.png)
![](bilder/polygonix_blocks_0_2_2.png)

#### Python

```python
import turtle
eingabe = input("Wieviele Ecken soll die Figur haben?")
eingabe_zahl = int(eingabe) #Konvertierung von Text in Zahl
turtle.pensize(4)
if eingabe_zahl == 3:
    turtle.pencolor('black')
    turtle.forward(100)
    turtle.right(120)
    turtle.pencolor('blue')
    turtle.forward(100)
    turtle.right(120)
    turtle.pencolor('black')
    turtle.forward(100)
    turtle.right(120)
else:
    if eingabe_zahl == 4:
        turtle.pencolor('black')
        turtle.forward(100)
        turtle.right(90)
        turtle.pencolor('blue')
        turtle.forward(100)
        turtle.right(90)
        turtle.pencolor('black')
        turtle.forward(100)
        turtle.right(90)
        turtle.pencolor('blue')
        turtle.forward(100)
        turtle.right(90)
    else:
        print("Das Programm unterstützt aktuell nur Dreiecke oder Vierecke.")
```
## POLYGONIX Version 0.3

### Algorithmisierung

#### Pseudocode

```python
Wir fragen den Benutzer nach der Anzahl der Ecken, konvertieren die Texteingabe in eine Zahl und merken uns die Zahl.
Wir definieren die Linienfarbe "black".
Wir definieren einen Zähler mit dem Startwert 0, der die Anzahl der Wiederholungen enthält.
Wir wiederholen solange der Zähler kleiner als die eingegebene Anzahl von Ecken ist:
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um (360 : anzahl_ecken) Grad
    Wir zählen den Zähler um 1 hoch.
```
#### Struktogramm
![](bilder/polygonix_0_3.png)

### Implementierung

#### Blöcke
![](bilder/polygonix_blocks_0_3.png)

#### Python

```python
import turtle
eingabe = input("Wieviele Ecken soll die Figur haben?")
eingabe_zahl = int(eingabe)
zaehler = 0
turtle.pensize(4)
turtle.pencolor('black')
while zaehler < eingabe_zahl:
    turtle.forward(100)
    turtle.right(360/eingabe_zahl)
    zaehler = zaehler + 1
```

## POLYGONIX Version 0.4

### Algorithmisierung

#### Pseudocode
```python
Wir fragen den Benutzer nach der Anzahl der Ecken, konvertieren die Texteingabe in eine Zahl und merken uns die Zahl.
Wir definieren einen Zähler mit dem Startwert 0, der die Anzahl der Wiederholungen enthält.
Wir wiederholen solange der Zähler kleiner als die eingegebene Anzahl von Ecken ist:
    Wenn der Zähler durch 2 teilbar ist (ergibt also Zähler dividiert durch 2 den Rest 0):
        Wir setzen die Linienfarbe "blue"
    Ansonsten:
        Wir setzen die Linienfarbe "black"
    Wir zeichnen eine Linie der Länge 100
    Wir drehen uns um (360 : anzahl_ecken) Grad
    Wir zählen den Zähler um 1 hoch.
```
#### Struktogramm

![](bilder/polygonix_0_4.png)

### Implementierung
#### Blöcke
![](bilder/polygonix_blocks_0_4.png)

#### Python
```python
import turtle
eingabe = input("Wieviele Ecken soll die Figur haben?")
eingabe_zahl = int(eingabe)
zaehler = 0
turtle.pensize(4)
while zaehler < eingabe_zahl:
    if zaehler % 2 == 0: # Rest bei Division durch 2 gleich 0?
        turtle.pencolor('blue')
    else:
        turtle.pencolor('black')
    turtle.forward(100)
    turtle.right(360/eingabe_zahl)
    zaehler = zaehler + 1
```
## POLYGONIX VERSION 1.0
### Algorithmisierung
#### Pseudocode
```python
Wir definieren eine Variable eingabe_ok und setzen diese auf False
Solange eingabe_ok nicht auf True gesetzt ist:
    Der Benutzer wird aufgefordert, eine Zahl größer gleich 3 einzugeben.
    Wir fersuchen die Eingabe in eine Zahl zu konvertieren.
    Wenn die Konvertierung gelingt:
        Wenn die Zahl größer gleich 3 ist:
            Es liegt eine korrekte Benutzereingabe vor. Wir setzen die Variable eingabe_ok auf True und verlassen damit die Schleife
        Sonst:
            Wir informieren den Benutzer darüber, dass nur Zahlen größer gleich 3 erlaubt sind
    Sonst:
        Konvertierung ist fehlgeschlagen. Wir informieren den Benutzer darüber, dass nur Zahlen erlaubt sind.
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
#### Struktogramm
![](bilder/polygonix_1_0.png)

### Implementierung
#### Blöcke
![](bilder/polybonix_blocks_1_0_1.png)
![](bilder/polybonix_blocks_1_0_2.png)

#### Python
```python
import turtle
zaehler = 0
eingabe_ok = False
eingabe_zahl = 0
while not eingabe_ok:
    try:
        eingabe = input("Wieviele Ecken soll die Figur haben?")
        eingabe_zahl = int(eingabe)
        if eingabe_zahl >= 3:
            eingabe_ok = True
        else:
            print("Es sind nur Zahlen größer oder gleich 3 erlaubt!")
    except:
        print("Bitte eine Zahl eingeben!")
turtle.pensize(4)
while zaehler < eingabe_zahl:
    if zaehler % 2 == 0:
        turtle.pencolor('blue')
    else:
        turtle.pencolor('black')
    turtle.forward(100)
    turtle.right(360/eingabe_zahl)
    zaehler = zaehler + 1
```