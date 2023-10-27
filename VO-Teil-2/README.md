# Inhalte VO Grundlagen der Programmierung (Termin 2)

## Betroffene Bildungsinhalte und Kompetenzen lt. HLG-Curriculum

### Vorlesung
Es werden schwerpunktmäßig folgende Bildungsinhalte des Curriculums in der Vorlesung behandelt:

* informatisches Denken und Informatische Arbeitsprinzipien (etwa Entwurfsprinzipien, strukturierte Programmierung, abstrakte Datentypen, Modularisierung, Hierarchisierung, Prototyping, Debugging)
* Entwicklungsprozesse (insbesondere agile Projekte)
* Programmierkonzepte (Variablen, Schleifen, Verzweigungen, Ereignisse, Prozeduren, Funktionen)

Es werden schwerpunktmäßig folgende Kompetenzen des Curriculums in der VO behandelt: 

* Teilbereiche des Informatischen Denkens benennen und Bezüge zur Lebenswelt von Schüler*innen herzustellen.
* informatische Arbeitsprinzipien zu erklären und damit Probleme zu analysieren, Problemlösungen unter Benutzung geeigneter Methoden zu beschreiben und diese zu realisieren.
* unterschiedliche Programmiersprachen-Paradigma und Darstellungsformen sowie deren Vor- und Nachteile im Schulunterricht zu benennen.
* unterschiedliche Programmierkonzepte in einer blockorientierten bzw. textorientierten Programmiersprache anzuwenden und zu reflektieren.
  
In den **Übungen zur VO** werden die Inhalte der VO anhand eines durchgängingen Beispiels und mit einem passenden Werkzeug illustriert. Dazu werden folgende Bildungsinhalte wiederholt: 

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

### Eigenleistung für die Übungen
Als Eigenleistung für die Übung wäre z.B. die Entwicklung eines durchgängigen Beispiels für den Schulunterricht sinnvoll. 

Eigenschaften:

* Unterrichtsplanung zur Einbettung des Beispiels im T-G-I-Rahmen mit Schwerpunkt auf:
  * Ziele lt. DGB-Curriculum
  * Lernzielkontrolle
  * Verlaufsplan / Methodik
* Beispiel (Angaben für Schüler:innen)
* Vollständige Implementierung / Lösung

Das Beispiel soll die wesentlichen Konzepte aus der VO Teil 1 und Teil 2 aufgreifen und mit einem Werkzeug implementiert werden, das in einer der Übungen verwendet wurde.

## Script zur VO Teil 2
1. Wiederholung der [Zentralen Ideen und Prozesse](../Didaktik/Zentrale-Ideen.md)
2. Verweis auf [Werkzeuge und Unterlagen](../Didaktik/Werkzeuge.md)
   1. Hinweis auf [Thonny](https://thonny.org)
   2. Hinweis auf [StructoG] (https://dditools.inf.tu-dresden.de/dev/struktog/)
3. [POLYGONIX](../VO-Teil-1/GrundkonzepteProgrammierung/Polygonix/README.md) 
   1. Das Beispiel zeigt die Anwendung zentraler Denkweisen, Entwicklungsprozesse und Konzepte der Programmierung
   2. Anhand einer realweltlichen Problemstellung wird von der Problemanalyse über die Algorithmisierung bis hin zur Implementierung in Python eine "Lern-App" mit Turtle-Grafik erzeugt.
4. POLYGONIX-Varianten
   1.  [Mit Listen und Zufall](../VO-Teil-2/TurtleBeispiele/vieleckFarbenArray.py)
   2.  [Mit Listen, Zufall und Methoden](../VO-Teil-2/TurtleBeispiele/vieleckFarbenArrayMethoden.py)
5. [Events mit Turtle](../VO-Teil-2/TurtleBeispiele/eventsMitTurtle.py) Programmierung der Turtle mit Events zur Steuerung der Turtle um ein kleines Zeichenprogramm zu simulieren.
6. [Events mit GUI](../VO-Teil-2/BMI/BmiV7.py) Beispiel für GUI-Programmierung mit Events in Python anhand der BMI-Berechnung.
7. [Neuronale Netze mit OpenRoberta](../VO-Teil-2/OpenRobertaNN/) Ein Beispiel für die Steuerung eines Roboters mit einem Neuronalen Netz
8. Todo: Events und Methoden am Beispiel Arcade-Game-Textadventure

## Weitere Beispiele zur Anregung
Die Liste der folgenden Beispiele kann als Anregung / Teillösung für die eigenen Projekte genutzt werden:

1. [Quadrat / Vielecke](../VO-Teil-1/GrundkonzepteProgrammierung/TurtleBeispiele/) in Python-Logo (blockbasiert)
   - Alternative Miniwelten (Karel, Scratch, Swift Playgrounds)
   - Pen-And-Paper-Spiele, wie z. B. die Robotersteuerung am Papier aus [micro:bit Schulbuch](https://microbit.eeducation.at/wiki/Hauptseite) auf den Seiten 11 bis 18
2. [Countdown](../VO-Teil-1/GrundkonzepteProgrammierung/Countdown/)
   - Problemanalyse
   - Codierung in Python
3. [Zahlenraten](../VO-Teil-1/GrundkonzepteProgrammierung/Zahlenraten/README.md)
   - Problemanalyse
   - Codierung in Python
   - Variante als Computerspiele für einen Handheld
   - Variante als Microcontroller-Programm
4. [Body Mass Index (BMI)](../VO-Teil-1/GrundkonzepteProgrammierung/BMI/README.md)
   - BMI als Excel-Lösung
   - BMI in 3 Iterationen mit Python
5. [Schere-Stein-Papier](../VO-Teil-1/GrundkonzepteProgrammierung/SchereSteinPapier/README.md)
6. [Tamagotchi](../VO-Teil-1/GrundkonzepteProgrammierung/Tamagotchi/README.md)

## Fortgeschrittene Beispiele zur Anregung
* [BMI extended](./BMI/)
  * In Mehreren weiteren "Iterationen" werden etwa die Konzepte Methoden und Events eingeführt.
* [Stadt-Land-Fluss](./StadtLandFluss/)
* [Textadventure](./Textadventure/)
* [Worteraten](./Worteraten/)
* [Zahlenraten mit Intelligenz](./ZahlenratenKI/)