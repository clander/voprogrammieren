# VO Programmieren - Skript

## Didaktische Überlegungen

Im Zentrum des Unterrichts steht ein informatischer Modellbildungsprozess zur Lösung authentischer Problemsituationen. Wir lösen ein Problem mithilfe des Computers, indem wir geistige und praktische Techniken der Informatik zur Anwendung bringen. Wir lernen dabei zentrale informatische Konzepte und Prozesse kennen und wir nutzen Werkzeuge der Informatik, um Lösungen für das Problem zu realisieren. Dadurch entwickeln wir ein Verständnis über den Aufbau und die Wirkungsweise von Informatiksystemen. Das wiederum ermöglicht uns Chancen und Grenzen der Nutzung von Informationssystemen zu erkennen, ein korrektes Weltbild aufzubauen, in einer mit IT durchsetzten Welt zu partizipieren sowie vernünftig, verantwortungsvoll und reflektiert mit den Technologien umzugehen.

Die Konzepte, Prozesse und Werkzeuge, die wir dabei für Lösungsfindung nutzen können, sind in der Informatik vielfältig. Zur Vermittlung zentraler geistiger sowie praktischer Techniken der Informatik eignen sich jedoch insbesondere Programmiersprachen.

Im Rahmen der Nutzung von Programmiersprachen zur Lösung von Problemen gibt es verschiedene „Werkzeugkästen“ - auch Paradigmen genannt, die wiederum unterschiedliche Modellierungstechniken betreffen und damit Lösungen auf unterschiedliche Arten ermöglichen. 

Ein etablierter Werkzeugkasten ist der Imperative (prozedural / objektorientiert). Er enthält viele fundamentale Ideen der Informatik, 
* die schon über sehr lange Zeit Gültigkeit haben,
* in vielen Teilgebieten des Faches (und auch in anderen Fachgebieten) verwendet werden,
* sich gut in der Lebenswelt unserer Schüler zeigen lassen, und
* in verschiedenen Komplexitätsniveaus (von der Primarstufe bis in die Tertiärstufe) vermittelt werden können

Konkret haben wir es im gewählten Werkzeugkasten uA mit folgenden Ideen und Konzepten zu tun:

* Quellcode (Compilezeit)
* Ausgeführtes Programm (Laufzeit)
* Ausdrücke (zB arithmetische oder bool‘sche Ausdrücke)
* Operatoren und Operanden
* Anweisungen
* Sequenzen von Anweisungen / Anweisungsblöcke
* Variablen
* Datentypen (Ganzzahlen, Kommazahlen, Texte)
* Sichtbarkeit / Gültigkeit
* Zuweisung
* Bedingte Verzweigung
* Wiederholung
* Datenstrukturen (Listen, Dictionaries)
* Modularisierung mit Funktionen / Prozeduren

Wichtig für die Vermittlung solcher Ideen sind uA folgende Prinzipien:

* Authentische Problemstellungen mit verschiedenen Kontexten
* Lernen am Modell
* Scaffolding und Fading
* Transfer einüben (primär durch Analogiebildung)
* Vom Abstrakten zum Konkreten zum Abstrakten
* Verhältnis zwischen Konzept, realisierendem Werkzeug und Anwendung im Rahmen der Problemlösung explizieren
* Hinweis auf historische Relevanz (und Personen dazu)
* Spiralprinzip, und damit
    * Symbolische, ikonische und enaktive Repräsentation
    * Vorwegnehmendes Lernen (Henne-Ei-Problem)
    * Fortsetzendes Lernen auf immer komplexeren Niveaus

Methodisch liegt der Fokus weiters auf Problemlösen durch Modellbildung und Simulation.

Die Vorgangsweise im Rahmen des informatischen Modellbildungsprozesses sieht mit Bezug auf die zentralen Ideen des CT dann wie folgt aus:

1. Problem Specification: analyze the problem and state it precisely, using abstraction, decomposition, and pattern recognition as well as establishing the criteria for solution
2. Algorithmic Expression: find a computational solution using appropriate data representations and algorithm design
3. Solution Implementation & Evaluation: implement the solution and conduct systematic testing before generalizing to other problems

Damit ergibt sich der zentrale informatische Lösungsprozess, ausgehend vom Problem (Startzustand), weiter über einen Weg durch den Problemraum (Zwischenzustände) hin zur fertigen Lösung (erwünschter Endzustand) durch folgenden an den Spftwareentwicklungszyklus angelehnten Prozess:

Problem => Plan (Konzepte) => (Teil-)Umsetzung (Werkzeuge) => Test => Syntaxcheck => Test => Debugging => Test => fertige Lösung

In der Planungsphase versuchen wir die Konzepte der Informatik zur Anwendung zu bringen, um einen Lösungsplan für unser Problem zu entwickeln. Dabei kommen verschiedene geistige Techniken der Informatik wie Abstraktion, Generalisieren, Dekomposition oder auch Mustererkennung zur Anwendung. 

* Abstraktion: Wir fokussieren auf die für die Lösung absolut notwendigen Lösungselemente und lassen alles andere weg. 
* Generalisierung: Wir versuchen eine Lösung zu finden, die nicht nur Spezialfälle von Problemen sondern eine Problemkategorie löst. 
* Dekomposition: Wir teilen das Problem in verschiedene Teilprobleme, die - jedes für sich genommen - durch die Anwendung unseres Lösungswerkzeuge lösbar sind. Wir überlegen uns, wie wir diese Teillösungen wieder zu einer Gesamtlösung zusammenbauen können.
* Mustererkennung: Wir halten nach Mustern und damit nach Automatisierungspotential Ausschau: immer wiederkehrende Lösungsteile lassen sich durch Programmiersprachen sehr schön abbilden.

Danach folgt die Beschreibung eines Lösungsalgorithmus. Wir verwenden dazu algorithmische Grundbausteine und passende Datenstrukturen. Die Beschreibung erfolgt über einfache (konzeptorientierte) Texte oder auch graphische Modelle. Im Bereich der imperativ-prozeduralen Programmierung eigenen sich Aktivitätsdiagramme, Struktogramme oder auch Zustandsdiagramme zur ikonischen Repräsentation von Algorithmen.

Nachdem wir unseren Lösungsalgorithmus geplant haben, gehen wir in die Umsetzung über. Dazu suchen wir ein Werkzeug, das es uns aufgrund der unterstützten Konzepte bzw. aufgrund des gewählten Modellierungsparadigmas ermöglicht, den Algorithmus umzusetzen, auszuführen und zu testen. 

Wir beginnen mit der Implementierung. Im Laufe der Implementierung werden wir als Anfänger Fehler machen. Fehler können z.B. die Syntax der Programmiersprache (das Programm lässt sich nicht starten) betreffen oder können sich in Form von semantischen Fehlern bzw. Bugs äußern (das Programm lässt sich starten, läuft, liefert aber die falschen Ergebnisse). Als Programmierer bessern wir diese Fehler aus. Ggf. kommen wir im Rahmen der Implementierung auch auf notwendige Anpassungen unseres Lösungsplanes.

In kurzen Zyklen werden wir so nach jeder kurzen Programmiertätigkeit immer wieder das Programm versuchen auszuführen. Wenn sich das Programm nicht starten lässt, analysieren wir die Fehlermeldungen des Interpreters / Compilers und bessern die Syntax aus. Wenn sich das Programm jedoch starten lässt, können wir kontrollieren, ob das Programm die richtigen (Teil-)Ergebnisse im Sinne unserer Problemstellung liefert. Dazu benötigen wir Techniken, die es uns ermöglichen in die Laufzeit eines Programmes hineinzuschauen bzw. Ergebnisse des Programmes anzuzeigen.

Wenn das Programm im Sinne der Ausgangsproblemstellung und des darauf definierten Lösungsalgorithmus korrekt funktioniert,  dann sind wird fertig. Handelt es sich nur um eine Teillösung, gehen wir zur Bearbeitung des nächsten Lösungsteils über.

Referenzen zum Thema Computational Thinking

* https://digitalpromise.org/initiative/computational-thinking/computational-thinking-for-next-generation-science/what-is-computational-thinking/
* https://towardsdatascience.com/computational-thinking-defined-7806ffc70f5e
* http://www.icompute-uk.com/news/computational-thinking-2/

## Beispiele für Mini-Projekte für Anfänger

* 5 Miniprojekte in Python für Anfänger: https://youtu.be/DLn3jOsNRVE 
* Hangman
* Textadventure Zork
* Madlips
* Zahlen raten
* Ki Zahlen raten / binäre Suche
* BMI mit Entscheidung
* PV Anlagenbau
* Ticketautomat
* HTML/SVG produzieren

## Unterlagen
### Python Referenz
https://www.w3schools.com/python/default.asp
https://docs.python.org/3/

### Python Bibliotheken
Python Turtle Graphics: https://docs.python.org/3/library/turtle.html
PyGame (Game Development): https://www.pygame.org/news
TkInter (GUI): https://docs.python.org/3/library/tkinter.html
Custom TkInter (GUI): https://github.com/TomSchimansky/CustomTkinter
Python Standard-Library: https://docs.python.org/3/library/index.html
Pygal (Charting) https://www.pygal.org/en/stable/
Requests (API-Requests): https://www.w3schools.com/python/module_requests.asp
Processing (Interaktive-Drawing-And-Multimedia): https://py.processing.org

### Tutorials
Python problem- und konzeptorientiert:
https://www.inf-schule.de/imperative-programmierung/python

### Python Bakery Videos
https://youtube.com/playlist?list=PLiK576qSavfIw_0ds6Z4JAzAyyj7b1SNE

### Python lernen in 4 Stunden
https://youtu.be/RBpK8C3N-Y8

### EinfachInfoPython Kurs
https://youtube.com/playlist?list=PLywzm7Lq4JoKvxNR7ROv_gJ09roJ-UDRt

### Socratia Python Tutorials:
https://youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-

### Schulbuch mit Projekten für den Microbit
https://microbit.eeducation.at/wiki/Hauptseite

## Entwicklungsumgebungen und Hilfswerkzeuge

### Blockbasierte Onlineumgebungen für Python
https://app.edublocks.org/editor
https://think.cs.vt.edu/blockpy/

### MakeCode
https://makecode.microbit.org

### Python Kara
https://www.swisseduc.ch/informatik/karatojava/pythonkara/index.html

### Python Hamstermodell
http://www.java-hamster-modell.de/python.html

### (Didaktische) IDEs
https://thonny.org
https://guipy.de/doku.php?id=start
https://www.tigerjython.ch/de/products/tigerjython-ide
https://www.jetbrains.com/pycharm/

### Structorizer IDE
https://help.structorizer.fisch.lu/index.php?menu=44&page=

### Sbide Structogramm IDE
https://www.sbide.de/?s=38sVWj

### Python Tutor
https://pythontutor.com

### Diagramme zeichnen
Mermaid: https://mermaid.live
PlantUML: https://plantuml.com


Skizzen zur Didaktik

￼
