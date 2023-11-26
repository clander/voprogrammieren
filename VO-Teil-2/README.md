# VO Grundlagen der Programmierung (Termin 2)

## TOC
1. Zentrale Konzepte und Prozesse
   - Kurze WH der Theorie
   - Praktische Umsetzung mit POLYGONIX (incl. WH der Inhalte vom VO Termin 1)
2. Neue Konzepte:
   - Arrays
   - Zufall
   - Funktionen
   - Ereignisse
   - Ausnahmebehandlung
3. Exkurs:
   - KI und Roboter-Programmierung

## Script
1. (**V**) [Zentrale Prozesse und zentrale Konzepte](../Didaktik/Zentrale-Ideen.md)
2. (**V**) [POLYGONIX](../VO-Teil-1/GrundkonzepteProgrammierung/Polygonix/README.md)
   - Das Beispiel zeigt anhand einer Problemstellung die Anwendung zentraler Denkweisen, Entwicklungsprozesse und Konzepte der Programmierung
   - [Weitere Turtle-Beispiele einfach](../VO-Teil-1/GrundkonzepteProgrammierung/TurtleBeispiele/)
   - [Weitere Turtle-Beispiele komplexer](../VO-Teil-2/TurtleBeispiele/)
3. Beispiele für neue Konzepte: Arrays und Zufall
   - (**V**) [POLYGONIX: Turtle Beispiel mit Array und Zufall](../VO-Teil-2/TurtleBeispiele/vieleckFarbenArray.py)
   - [Zahlenraten (auch mit microBit)](../VO-Teil-1/GrundkonzepteProgrammierung/Zahlenraten/README.md)
   - [Worte erraten](../VO-Teil-2/Worteraten/HangMan.py)
   - (**UE**)[Stadt-Land-Fluss (auch mit microBit)](../VO-Teil-2/StadtLandFluss/)
   - [Schere-Stein-Papier Variante mit Arrays](../VO-Teil-1/GrundkonzepteProgrammierung/SchereSteinPapier/SchereSteinPapier.py)
   - [Wetterstation](../VO-Teil-2/Wetterstation/Wetterdaten.py)
   - (**UE**)[Scharade-Variante mit MakeCode micro:bit](../VO-Teil-2/Scharade/README.md)
4. Beispiele für neues Konzept: Funktionen
   - (**V**) [POLYGONIX: Turtle Beispiel mit zwei Funktionen](../VO-Teil-2/TurtleBeispiele/vieleckFarbenArrayZweiMethoden.py) für zufällige Farbe und Eingabe incl. Validierung
   - (**V**) [POLYGONIX: Turtle Beispiel komplett modularisiert](../VO-Teil-2/TurtleBeispiele/vieleckFarbenArrayMethoden.py)
   - (**UE**) [Textadventure](./Textadventure/TextAdventure.py) Ein Textadventure vollständig mit Funktionen modularisiert, das eine kleine Story erzählt, dir nur mit informatischen Kenntnissen gelöst werden kann.
5. Neues Konzept: Ereignisse und Ereignisbehandlung
   - Ereignisse und deren Behandlung sind in vielen blockbasierten Entwicklungsumgebungen für Programmieranfänger (MakeCode, Scratch, AppInventor etc.) als eigene Blöcke / Kategorien verfügbar(siehe z.B. in Scratch die Kategorie "Ereignisse")
   - [Turtle als Zeichenprogramm](../VO-Teil-2/TurtleBeispiele/eventsMitTurtle.py) Programmierung der Turtle mit Events zur Steuerung der Turtle um ein kleines Zeichenprogramm zu simulieren.
   - Microsoft Arcade: Chase The Pizza Tutorial https://arcade.makecode.com/ -> Anleitungen -> Chase the Pizza: Programmierung eines kleinen Spiels mit der Microsoft Arcade Plattform (Events, Random, High-Level-Funktionen der Arcade-Plattform)
   - [BMI-Berechnung mit GUI](../VO-Teil-2/BMI/BmiV7.py) Beispiel für GUI-Programmierung mit Events in Python anhand der BMI-Berechnung.
6. Exkurs: OpenRoberta und KI
   - [Neuronale Netze mit OpenRoberta](../VO-Teil-2/OpenRobertaNN/) Beispiel für die Steuerung eines Roboters mit einem neuronalen Netz.
   - [Orange Datamining](https://orangedatamining.com)
7. Hinweise auf einige Tools und Online-Unterlagen:
   - [Structog](https://dditools.inf.tu-dresden.de/dev/struktog/) Struktogramm-Editor
   - [Python Tutor](https://pythontutor.com) Visualisierung von Python-Code-Ausführung
   - [Open Roberta Lab](https://www.roberta-home.de/lab/) Online-Ide für die Programmierung von Robotern und Microcontrollern (incl. Online-Sim und Unterstützung für Neuronale Netze)
   - [Thonny IDE](https://thonny.org) Spezielle Pyhton-IDE für Anfänger
   - [Microsoft MakeCode Arcade](https://arcade.makecode.com):
     - [Einführung in die Informatik 1](https://arcade.makecode.com/courses/csintro1)
     - [Einführung in die Informatik 2](https://arcade.makecode.com/courses/csintro2)
     - [Einführung in die Informatik 3](https://arcade.makecode.com/courses/csintro3)
   - [Microsoft MakeCode microBit](https://microbit.makecode.com):
     - [Einführung in die Informatik](https://makecode.microbit.org/courses/csintro)
   - [inf-schule.de](https://www.inf-schule.de/imperative-programmierung/python) Python, Fachkonzepte, Miniprojekte

## Weitere Beispiele zur Anregung
Die Liste der folgenden Beispiele kann als Anregung / Teillösung für die eigenen Projekte genutzt werden:

1. [Quadrat / Vielecke](../VO-Teil-1/GrundkonzepteProgrammierung/TurtleBeispiele/) in Python-Logo (blockbasiert)
   - Alternative Miniwelten (Karel, Scratch, Swift Playgrounds)
   - Pen-And-Paper-Spiele, wie z. B. die Robotersteuerung am Papier aus [micro:bit Schulbuch](https://microbit.eeducation.at/wiki/Hauptseite) auf den Seiten 11 bis 18
2. [Countdown](../VO-Teil-1/GrundkonzepteProgrammierung/Countdown/)
   - Problemanalyse
   - Codierung in Python
3. [Body Mass Index (BMI)](../VO-Teil-1/GrundkonzepteProgrammierung/BMI/README.md)
   - [BMI als Excel-Lösung](../VO-Teil-1/GrundkonzepteProgrammierung/BMI/BmiExcelLoesung.xlsx)
   - BMI in 3 Iterationen mit Python
5. [BMI extended](./BMI/) In weiteren "Iterationen" werden etwa die Konzepte "Funktionen" "GUIs" oder "Events" eingeführt.
6. [Textadventure](./Textadventure/)
7. [Zahlenraten mit Intelligenz](./ZahlenratenKI/) Man spielt gegen eine KI Zahlen raten. Die KI rät möglichst effizient (binäre Suche).
8. [Tamagotchi](../VO-Teil-1/GrundkonzepteProgrammierung/Tamagotchi/README.md) Dieses Beispiel zeigt neben der Implementierung auch die Erstellung eines Selbstlerntutorials mithilfe des Microsoft Makecode Tutorial Editors.

## Anregungen für die Eigenleistung / Übungsinhalte
- siehe [Methodik-Teil](../Didaktik/Methodik.md)

## ANHANG: Betroffene Bildungsinhalte und Kompetenzen lt. HLG-Curriculum

### Vorlesung
Schwerpunktmäßig werden in der VO folgende Bildungsinhalte des Curriculums behandelt:

* informatisches Denken und Informatische Arbeitsprinzipien (etwa Entwurfsprinzipien, strukturierte Programmierung, abstrakte Datentypen, Modularisierung, Hierarchisierung, Prototyping, Debugging)
* Entwicklungsprozesse (insbesondere agile Projekte)
* Programmierkonzepte (Variablen, Schleifen, Verzweigungen, Ereignisse, Prozeduren, Funktionen)

Es werden schwerpunktmäßig folgende Kompetenzen des Curriculums in der VO behandelt: 

* Teilbereiche des Informatischen Denkens benennen und Bezüge zur Lebenswelt von Schüler*innen herzustellen.
* informatische Arbeitsprinzipien zu erklären und damit Probleme zu analysieren, Problemlösungen unter Benutzung geeigneter Methoden zu beschreiben und diese zu realisieren.
* unterschiedliche Programmiersprachen-Paradigma und Darstellungsformen sowie deren Vor- und Nachteile im Schulunterricht zu benennen.
* unterschiedliche Programmierkonzepte in einer blockorientierten bzw. textorientierten Programmiersprache anzuwenden und zu reflektieren. 

### Übungen zur Vorlesung
In den Übungen zur Vorlesung Teil 2 werden die Inhalte der VO aufgegriffen und anhand eines durchgängigen Beispiels sowie einer passenden Entwicklungsumgebung zur Anwendung gebracht.

Betroffene Bildungsinhalte des HLG-Curriculums:

* Entwicklungsumgebungen im schulischen Kontext und deren Unterrichtsrelevanz
* blockorientierte und textbasierte Programmiersprachen
* Roboter, Ein-Platinen-Rechner und andere elektronischen Materialien des informatischen Denkens

Betroffene Kompetenzen aus dem HLG-Curriculum:

* gängige Entwicklungsumgebungen zu nennen, und wissen über deren Vor- und Nachteile Bescheid.
* Programmiersprachen in kreativer Art und Weise zur Verwirklichung von Projekten zu nutzen.
* klassische und agile Entwicklungsmethoden zu nennen und diese im Schulunterricht mit den Schüler*innen in Projekten umzusetzen.
* ein im Kontext der Modulinhalte zu verortendes, didaktisch und fachdidaktisch begründetes Projekt mit Robotern, Ein-Platinen-Rechner oder anderen elektronischen Materialien des informatischen Denkens, zu planen, umzusetzen und die erstellten Unterrichtsszenarien kritisch zu reflektieren.