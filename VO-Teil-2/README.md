# Inhalte VO Grundlagen der Programmierung (Termin 2)

## Betroffene Bildungsinhalte und Kompetenzen lt. HLG-Curriculum

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

## Script zur VO Teil 2
1. Wiederholung der [Zentralen Ideen und Prozesse](../Didaktik/Zentrale-Ideen.md)
2. Verweis auf [Werkzeuge und Unterlagen](../Didaktik/Werkzeuge.md)
   1. Hinweis auf [Thonny](https://thonny.org)
   2. Hinweis auf [StructoG](https://dditools.inf.tu-dresden.de/dev/struktog/)
3. [POLYGONIX](../VO-Teil-1/GrundkonzepteProgrammierung/Polygonix/README.md) 
   1. Das Beispiel zeigt die Anwendung zentraler Denkweisen, Entwicklungsprozesse und Konzepte der Programmierung
   2. Anhand einer realweltlichen Problemstellung wird von der Problemanalyse über die Algorithmisierung bis hin zur Implementierung in Python eine "Lern-App" mit Turtle-Grafik erzeugt.
4. POLYGONIX-Varianten
   1.  [Mit Listen und Zufall](../VO-Teil-2/TurtleBeispiele/vieleckFarbenArray.py)
   2.  [Mit Listen, Zufall und Methoden](../VO-Teil-2/TurtleBeispiele/vieleckFarbenArrayMethoden.py)
5. [Turtle als Zeichenprogramm](../VO-Teil-2/TurtleBeispiele/eventsMitTurtle.py) Programmierung der Turtle mit Events zur Steuerung der Turtle um ein kleines Zeichenprogramm zu simulieren.
6. Chase The Pizza Tutorial: https://arcade.makecode.com/-> Anleitungen -> Chase the Pizza: Programmierung eines kleinen Spiels mit der Microsoft Arcade Plattform (Events, Random, High-Level-Funktionen der Arcade-Plattform)
7. [BMI-Berechnung mit GUI](../VO-Teil-2/BMI/BmiV7.py) Beispiel für GUI-Programmierung mit Events in Python anhand der BMI-Berechnung.
8. [Neuronale Netze mit OpenRoberta](../VO-Teil-2/OpenRobertaNN/) Ein Beispiel für die Steuerung eines Roboters mit einem neuronalen Netz.

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
  * In weiteren "Iterationen" werden etwa die Konzepte Methoden und Events eingeführt.
* [Stadt-Land-Fluss](./StadtLandFluss/)
* [Textadventure](./Textadventure/)
* [Worteraten](./Worteraten/)
* [Zahlenraten mit Intelligenz](./ZahlenratenKI/)

## Anregungen für die Eigenleistung
1. Problemstellung:
   - Suche eine passende Problemstellung (passend zum gewählten Werkzeug, passend zum Transport der Konzepte und Prozesse der VO / des DGB-Lehrplanes)
   - Beispiele:
     - Anregungen für Projekte siehe VO / siehe oben, weiters:
     - [Miniprojekte auf Inf-Schule.de](https://www.inf-schule.de/imperative-programmierung/python/projekte)
     - Beispielprojekte aus programmierkonzepte.ch
       - [TigerJython-Projekt](https://www.tigerjython.ch/de/tutorials)
       - [TigerJython for Kids](https://www.tigerjython4kids.ch)
       - [Programmierkonzepte](https://programmierkonzepte.ch)
       - [Grafik, Robotik, Datenbanken, Spiele](https://www.jython.ch)
       - [Python online](https://python-online.ch)
     - [Schulbuch](https://microbit.eeducation.at/wiki/Hauptseite)
     - [Unterlagen für weitere Projektideen](../../../Didaktik/README.md)
2. Tutorial:
   - Erstelle eine fertige Anleitung zur Lösung der ersten Problemstellung.
   - Die Lösung soll iterativ in mehreren Teillösungen / Versionen erfolgen.
   - Die Lösung soll die zentralen Konzepte verwenden, darunter:
     - Anweisungen
     - Blöcke
     - Variablen
     - Operatoren
     - Bedingungen
     - Verzweigungen
     - Schleifen
     - evtl. Listen
     - evtl. Funktionen
     - evtl. Zufallszahlen
     - evtl. Events
     - usw ... siehe POLYGONIX-Beispiel, siehe aber auch die Liste mit den [Zentralen Konzepten und Prozessen](../Didaktik/Zentrale-Ideen.md)
   - Evtl. findet sich eine Problemstellung im Bereich KI?
   - Für jede Teillösung / Version / Iteration wird folgender Zyklus durchlaufen (siehe dazu auch [die zentralen Ideen der Programmierung im Unterricht](../../../Didaktik/Zentrale-Ideen.md))
     - Problemanalyse
       - Dekomposition
       - Abstraktion
       - Mustererkennung
       - Generalisierung
     - Algorithmisierung
       - Sprachkonzepte identifizieren und einführen
       - Struktogramm / Flussdiagramm zeichnen
       - Pseudocode formulieren
     - Implementierung und Test
       - mit IDE und Sprache der Wahl Pseudocode umsetzen
       - Testen
       - Debuggen
3. Zweite Problemstellung:
   - Das zweite Beispiel soll mit denselben Konzepten und Prozessen lösbar sein, jedoch eine völlig andere Fachdomäne betreffen. Es soll weniger Hilfestellungen beinhalten.
   - Dieses Beispiel dient dem Einüben von Transfer.
4. Erstelle eine kleine Unterrichtsplanung dazu:
   - Zielehierarchie
     - ausgehend vom Lehrplan
     - zentrale Konzepte / Ideen ableiten
     - Transferziel, Erkenntnisziel, Fakten, Fertigkeiten ableiten
   - Lernzielkontrolle 
     - in Form einer ähnlichen Problemstellung (Fokus Transfer)
     - Fokussiert auf die umfassende Kontrolle der Zieldimension
   - Stundenverlauf
     - Kern des Stundenverlaufs ist die Bearbeitung der beiden Beispiele / Problemstellungen.
     - Die didaktische Einbettung kann z. B. über ein klassisches didaktisches Design erfolgen, z.B [Gagné](https://www.niu.edu/citl/resources/guides/instructional-guide/gagnes-nine-events-of-instruction.shtml).
        1. Aufmerksamkeit erregen
        2. Ziele bekannt geben
        3. Vorwissen aktivieren
        4. Input (Konzepte + Werkzeuge)
        5. Lerngerüste
        6. Übungsphasen
        7. Feedback
        8. Kompetenzcheck
        9. Transfer einüben