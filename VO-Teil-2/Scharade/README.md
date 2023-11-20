# SHARADE

## Problemstellung (GRASPS-Schema)

### Ziel (Goal)
Implementiere [Scharade](https://de.wikipedia.org/wiki/Scharade_(Pantomimespiel)) mit dem Micro:bit.

### Deine Rolle (Role) / Situation (S)
Du bist Schüler:in im Fach Digitale Grundbildung. Dort lernst du, wie man kleine Computerprogramme für den Micro:bit schreibt. Du setzte die Kompetenzen aus dem Unterricht ein, um ein kurzweiliges Spiel für die Pause zu entwickeln.

### Deine Zielgruppe (Audience)
Du selbst und deine Klassenkameraden möchten das Spiel mit dem Micro:bit hin und wieder zum Zeitvertreib in der Pause spielen

### Das Produkt (Product, Purpose)

#### Funktionale Anforderungen der verschiedenen Iterationen

Folgende Benutzer:innen-Erfahrung soll in verschiedenen Versionen realisiert werden:

* V 0.1:
  * Benutzer:innen möchten den Micro:bit verwenden können, um mit einem Druck auf den A-Button eine Runde zu starten. In einer Runde wird zunächst nur ein zufälliges Wort aus einer größeren Liste von Wörtern angezeigt.
* V 0.2:
  * Zusätzlich zum zufälligen Begriff soll für jede Runde auch die Darstellungsart (Z für Zeichnen, P für Pantomime, E für Erklären) zufällig gewählt und angezeigt werden.
* V 0.3:
  * Benutzer:innen möchten, dass nach dem Start einer Runde und damit nach der Anzeige des Ratewortes ein Timer startet. Wenn der Timer abgelaufen ist, ist die Runde zu Ende. Das Wort muss vor Ablauf der Runde erraten werden.
* V 0.4:
  * Benutzer:innen möchten mit zwei Teams spielen können, deren Punktestand mitgeführt wird.
  * Das Team, das an der Reihe ist, soll mit "T1" oder "T2" angezeigt werden. Mit jeder neuen Runde wechseln die Teams.
  * Wenn ein Team vor Ablauf der Ratezeit den Begriff errät, kann das durch einen Druck auf den B-Button signalisiert werden. Dann soll für das aktuelle Team der Punktestand um 1 erhöht werden.
  * Wenn der Micro:bit geschüttelt wird, wird der Punktestand für beide Teams angezeigt.
* V 0.5:
  * Es soll ein neuer Schwierigkeitsgrad für Begriffe eingeführt werden. 
  * Das Programm soll mit jeder Runde entscheiden, ob ein Begriff aus dem Schwierigkeitsgrad "Normal" oder ein Begriff aus dem Schwierigkeitsgrad "Schwer" gewählt wird. Für eine erfolgreiche schwere Runde bekommt ein Team 2 Punkte. Für eine erfolgreiche leichte Runde bekommt ein Team 1 Punkt.
* V 0.5:
  * ...

## V 0.1

### Problemanalyse und Lösungsansatz
Generalisierung, Abstraktion, Mustererkennung, Lösungsansatz

### Algorithmisierung
Pseudocode, graphische Darstellung

### Implementierung
Blöcke oder Code

## V 0.2

### Problemanalyse und Lösungsansatz
Generalisierung, Abstraktion, Mustererkennung, Lösungsansatz

### Algorithmisierung
Pseudocode, graphische Darstellung

### Implementierung
Blöcke oder Code

## V ...

...

# Anhang mit Test-Prototypen (wird später gelöscht)

## Blöcke
![](./scharademicrobit.png)

## Python Code

```python
def on_button_pressed_a():
    global index
    if index >= 0 and index < len(woerter):
        countdownAnzeigen(3)
        basic.show_string("..." + woerter[index])
        index += 1
    else:
        basic.show_string("Ende")
input.on_button_pressed(Button.A, on_button_pressed_a)

def countdownAnzeigen(startenVon: number):
    global i
    basic.show_leds("""
        . # # # .
        . . . # .
        . . # # .
        . . . . .
        . . # . .
        """)
    basic.pause(200)
    i = startenVon
    while i >= 0:
        basic.pause(100)
        basic.show_number(i)
        i += -1
i = 0
woerter: List[str] = []
index = 0
index = 0
woerter = ["Katze", "Gitarre"]



````
``

