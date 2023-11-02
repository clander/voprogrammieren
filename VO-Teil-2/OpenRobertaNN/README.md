# OpenRoberta und Neuronale Netze

Die folgende Idee stammt aus einem c't-Artikel in der Ausgabe 24/2023 vom 21.10.2023. Das komplette Unterrichtsmaterial ist über folgenden c't-Link verfügbar:

[Materialien für den Unterricht auf c't Ausgabe 24 vom 21.10.2023](https://ct.de/ycc9)

Grundidee: Ein Roboter wird nicht über klassische Programmierung programmiert, sondern über ein neuronales Netz gesteuert. Dazu wird ein neuronales Netz konfiguriert. Die Eingangswerte für das Netz liefert der Roboter über seine Sensoren, die berechneten Werte der Neuronen steuern die Motoren des Roboters. 

Fortgeschritten: Das Netz kann auch trainiert werden. Sensorwerte des Roboters können z. B. für die Anpassung der Kantengewichte oder der Grundtendenz (Bias) verwendet werden.

## Annäherung an den Line-Follower:
Als Endergebnis programmieren die Kinder einen Line-Follower-Roboter.

- Grundidee:
  - Der Lichtsensor liefert die Eingeabewerte für das Eingangsneuron des neuronalen Netzes.
  - Die Ausgangsneuronen liefern die Werte für die Steuerung der Motoren des Roboters. 
  - Aktivierungsfunktion für die Ausgangsneuronen: "Linear"
- Erstes Experiment: 
  - Unveränderte Weitergabe des Eingangswertes für das Licht (100 für Weiß, 0 für Schwarz) an das Ausgangsneuron mit Kantengewicht 1. 
  - D.h. der Roboter stoppt auf Schwarz, und fährt auf Weißt mit voller Geschwindigkeit.
- Zweites Experiment: 
  - Graustufenbild. Roboter bewegt sich schneller, je heller, und langsamer je dunkler der Hintergrund. 
  - Live-Sensordaten geben Aufschluss über das Verhalten.
- Weitere Experimente (Exploration): 
  - Roboter 20 % schneller fahren lassen
  - Anpassung der Grundtendenz (Bias) 
  - Anpassung der Kantengewichte
  - Umkehren des Verhaltes des Roboters: Kantengewicht -1 und Grundtendenz 100.
- Hinweis für die Experimente:
  - Es gibt einen Debugger, der es ermöglicht, die Ausführung der Programmblöcke live mitzuverfolgen. (Achtung: der Debugger führt zu höherem CPU-Verbrauch und verndert damit die Simulation)
  - Sensorwerte und Variablenwerte können über eine gesonderte Ansicht zur Laufzeit mitverfolgt werden.

## Line Follower:
- Lösungsidee: Helligkeitssensor misst möglichst immer die Hälfte Schwarz und Weiß, also 50 Prozent Helligkeit.
- Festlegung: Schwarze Linie in Fahrtrichtung rechts, weiße Umgebung in Fahrtrichtung links.
- Wenn gemessene Helligkeit steigt (über 50 Prozent): Motor fürs linke Rad schneller drehen, Motor fürs rechte Rad langsamer drehen -> Rechtskurve.
- Wenn gemessene Helligkeit sinkt (unter 50 Prozent): Motor fürs rechte Rad schneller drehen, Motor fürs linke Rad langsamer drehen -> Linkskurve.
- Diskussion: 
  - könnte man das nicht einfach direkt algorithmisch programmieren? 
  - Zweck: Neuronale Netze und ihren Einsatz kennenlernen.
- Ausblick: 
  - So einfache Netze sind schon so komplex; Was wenn die Netze viel größer und viel tiefer werden?
- Ausblick: Man könnte den Roboter selbst lernen lassen, indem man die Grundtendenz bzw. die Kantegewichte per Feedback anpasst.

## Lösung
### Neuronales Netz
![Neuronales Netz](./OpenRobertaNN.png)

### Roboterkonfig
![RoboterKonfiguration](./OpenRobertaRobotconfig.png)

### Roboter-Programmierung mit Werten aus dem neuronalen Netz
![RoboterKonfiguration](./OpenRobertaProgramming.png)

## Weitere einfache Übungen
- Bewässerungsroboter soll sich langsamer über die grauen und gelben Stellen eines Rasens bewegen, um diese stärker zu bewässern.
- Roboter verhält sich wie ein Insekt, das seine Bewegungen den Lichtverhältnissen anpasst (Bewegung in Richtung Licht schneller)
- ...