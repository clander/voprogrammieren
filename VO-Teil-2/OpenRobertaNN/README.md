# OpenRoberta und Neuronale Netze

Die folgende Idee stammt aus einem c't-Artikel in der Ausgabe 24/2023 vom 21.10.2023 (Autoren: Michael Langwald, Florian Schuppan, artin Tilmans).

Das komplette Unterrichtsmaterial ist über folgenden Link verfügbar:

[Materialien für den Unterricht auf c't Ausgabe 24 vom 21.10.2023](https://ct.de/ycc9)

Grundidee: Es werden neuronale Netze konfiguriert. Die Eingangswerte für die Nezte liefert der Roboter über seine Sensoren, die berechneten Werte der Neuronen steuern die Motoren des Roboters.

Der Roboter wird also nicht über klasse Programmierung programmiert, sondern er wird über das neuronale Netz gesteuert.

## Annäherung an den Line-Follower:
Als Endergebnis programmieren die Kinder einen Line-Follower.

Dazu erledigen sie Schritt für Schritt immer komplexere Aufgaben:

- Programmierung des Roboters mit einem neuronalen Netz sodass er der schwarzen Linie entlangfährt. Der Lichtsensor liefert die Eingeabewerte für das neuronale Netz, die Ausgangsneuronen liefern die Eingabewerte für die Motorensteuern.
- Zuerst: Unveränderte Weitergabe des Eingangswertes für das Licht (100 für Weiß, 0 für Schwarz) an das Ausgangsneuron mit Kantengewicht 1. D.h. der Roboter stoppt auf Schwarz, und fährt auf Weißt mit voller Geschwindigkeit.
- Dann: Graustufenbild: Roboter bewegt sich schneller, je heller, und langsamer je dunkler der Hintergrund. Live-Sensordaten geben Aufschluss über das Verhalten.
- Weitere Experimente: z.B. Roboter 20 % schneller fahren lassen -> Anpassung der Grundtendenz bzw. der Kantegewischte (Exploration)
- Wie lässt sich das Verhalten des Roboters umkehren? Kantengewicht -1 und Grundtendenz 100.

## Line Follower:
- Lösungsidee: Helligskeitssensor misst möglichst immer die Hälfte Schwarz und Weiß, also 50 Prozent Helligkeit.
- Festlegung: Schwarze Linie in Fahrtrichtung rechts, weiße Umgebung in Fahrtrichtung links.
- Wenn gemessene Helligkeit steigt (über 50 Prozent): Motor fürs Linke Rad schneller drehen, Motor fürs rechte Rad langsamer drehen -> Rechtskurve.
- Wenn gemessene Helligkeit sinkt (unter 50 Prozent): es passiert das Gegenteil.
- Diskussion: könnte man das nicht einfach direkt algorithmisch programmieren? Zweck: Neuronale Netze und ihren Einsatz kennen lernen.
- Ausblick: so einfache Netze schon so komplex, was wenn die Netze viel größer werden?
- Ausblick: Man könnte den Roboter selbst lernen lassen, indem man die Grundtendenz bzw. die Kantegewichte solange per Feedback anpasst, bis der Roboter immer nur auf Grau fährt (50 %)

## Lösung
### Neuronales Netz
![Neuronales Netz](./OpenRobertaNN.png)

### Roboterkonfig
![RoboterKonfiguration](./OpenRobertaRobotconfig.png)

### Roboter-Programmierung mit Werten aus dem neuronalen Netz
![RoboterKonfiguration](./OpenRobertaProgramming.png)

## Weitere einfache Übungen
- Bewässerungsroboter soll sich langsamer über die blauen und gelben Stellen eines Rasens bewegen, um diese stärker zu bewässern.
- Roboter mimt ein Insekt, das seine Bewegungen den Lichtverhältnissen anpasst (Bewegung in Richtung Licht schneller)
- ...