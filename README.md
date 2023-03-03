# VO Programmieren - Skript

## Didaktische Überlegungen

### Modellbildung
Im Zentrum des Unterrichts steht ein informatischer Modellbildungsprozess zur Lösung authentischer Problemsituationen. Wir lösen ein Problem mithilfe des Computers, indem wir geistige und praktische Techniken der Informatik zur Anwendung bringen. Wir lernen dabei zentrale informatische Konzepte und Prozesse kennen und wir nutzen Werkzeuge der Informatik, um Lösungen für das Problem zu realisieren. Dadurch entwickeln wir ein Verständnis über den Aufbau und die Wirkungsweise von Informatiksystemen. Das wiederum ermöglicht uns Chancen und Grenzen der Nutzung von Informationssystemen zu erkennen, ein korrektes Weltbild aufzubauen, in einer mit IT durchsetzten Welt zu partizipieren sowie vernünftig, verantwortungsvoll und reflektiert mit den Technologien umzugehen.
### Zentrale Konzepte der Programmierung
Die Konzepte, Prozesse und Werkzeuge, die wir dabei für Lösungsfindung nutzen können, sind in der Informatik vielfältig. Zur Vermittlung zentraler geistiger sowie praktischer Techniken der Informatik eignen sich jedoch insbesondere Programmiersprachen.

Im Rahmen der Nutzung von Programmiersprachen zur Lösung von Problemen gibt es verschiedene „Werkzeugkästen“ - auch Paradigmen genannt, die wiederum unterschiedliche Modellierungstechniken betreffen und damit Lösungen auf unterschiedliche Arten ermöglichen. 

Ein etablierter Werkzeugkasten ist der Imperative (prozedural / objektorientiert). Er enthält viele fundamentale Ideen der Informatik, 
* die schon über sehr lange Zeit Gültigkeit haben,
* in vielen Teilgebieten des Faches (und auch in anderen Fachgebieten) verwendet werden,
* sich gut in der Lebenswelt unserer Schüler zeigen lassen, und
* in verschiedenen Komplexitätsniveaus (von der Primarstufe bis in die Tertiärstufe) vermittelt werden können

Konkret haben wir es im gewählten Werkzeugkasten uA mit folgenden Ideen und Konzepten zu tun:

* Quellcode (Compilezeit)
* ausgeführtes Programm (Laufzeit)
* Ausdrücke (z. B. arithmetische oder bool‘sche Ausdrücke)
* Operatoren und Operanden
* Anweisungen
* Sequenzen von Anweisungen / Anweisungsblöcke
* Variablen
* Datentypen (Ganzzahlen, Kommazahlen, Texte)
* Sichtbarkeit / Gültigkeit
* Zuweisung
* bedingte Verzweigung
* Wiederholung
* Datenstrukturen (Listen, Dictionaries)
* Modularisierung mit Funktionen / Prozeduren

Wichtig für die Vermittlung solcher Ideen sind uA folgende Prinzipien:

* Authentische Problemstellungen mit verschiedenen Kontexten
* Lernen am Modell
* Scaffolding und Fading
* Transfer einüben (primär durch Analogiebildung)
* Vom Abstrakten zum Konkreten wieder zum Abstrakten
* Verhältnis zwischen Konzept, realisierendem Werkzeug und Anwendung im Rahmen der Problemlösung explizieren
* Hinweis auf historische Relevanz (und Personen dazu)
* Spiralprinzip, und damit
    * Symbolische, ikonische und enaktive Repräsentation
    * vorwegnehmendes Lernen (Henne-Ei-Problem)
    * fortsetzendes Lernen auf immer komplexeren Niveaus

### Zentrale Prozesse der Programmierung
Methodisch liegt der Fokus weiters auf Problemlösen durch Modellbildung und Simulation.

Die Vorgangsweise im Rahmen des informatischen Modellbildungsprozesses sieht mit Bezug auf die zentralen Ideen des Computational Thinking dann wie folgt aus:

1. Problemanalyse
2. Algorithmisierung
3. Implementierung und Test

Wichtig ist zu verstehen, dass es sich bei den oben genannten drei Punkten um einen Zyklus handelt, der immer wieder durchlaufen wird, solange, bis das Problem gelöst ist. Ausgehend vom Problem (Startzustand), über einen Weg durch den Problemraum (Zwischenzustände) hin zur fertigen Lösung (erwünschter Endzustand) ergibt sich damit eine an den Softwareentwicklungszyklus angelehnte zyklische Vorgehensweise. 

### Problemanalyse
Das Problem wird analysiert und möglichst präzise formuliert. Dazu werden Techniken wie Abstraktion, Dekomposition oder Mustererkennung angewendet. Außerdem wird genau spezifiziert, wann das Problem als gelöst angesehen wird (Kriterien).

* Abstraktion: Wir fokussieren auf die für die Lösung absolut notwendigen Lösungselemente und lassen alles andere weg. 
* Generalisierung: Wir versuchen eine Lösung zu finden, die nicht nur Spezialfälle von Problemen, sondern eine Problemkategorie löst. 
* Dekomposition: Wir teilen das Problem in verschiedene Teilprobleme. Wir überlegen uns, wie wir diese Teillösungen wieder zu einer Gesamtlösung zusammenbauen müssen.
* Mustererkennung: Wir halten nach Mustern und damit nach Automatisierungspotential Ausschau: immer wiederkehrende Lösungsteile lassen sich durch Programmiersprachen sehr effizient implementieren.
* Lösungsspezifikation: Wir definieren möglichst genaue "Abnahmekriterien" für eine Lösung 
### Algorithmisierung
Danach folgt die Beschreibung eines Lösungsalgorithmus. Wir verwenden dazu algorithmische Grundbausteine und passende Datenstrukturen. 

> Ein Algorithmus (benannt nach Al-Chwarizmi, von arabisch: الخوارزمی al-Ḫwārizmī, deutsch ‚der Choresmier‘) ist eine eindeutige Handlungsvorschrift zur Lösung eines Problems oder einer Klasse von Problemen. Algorithmen bestehen aus endlich vielen, wohldefinierten Einzelschritten. Damit können sie zur Ausführung in ein Computerprogramm implementiert, aber auch in menschlicher Sprache formuliert werden. Bei der Problemlösung wird eine bestimmte Eingabe in eine bestimmte Ausgabe überführt. (https://de.wikipedia.org/wiki/Algorithmus)

Die Beschreibung des Algorithmus erfolgt über einfache (konzeptorientierte) Texte oder auch ikonische / grafische Darstellungen. Im Bereich der imperativ-prozeduralen Programmierung eigenen sich 
* Aktivitätsdiagramme (Flussdiagramme)
* Struktogramme
* Zustandsdiagramme

Nachdem wir unseren Lösungsalgorithmus geplant haben, gehen wir in die Umsetzung über. Dazu suchen wir ein Werkzeug, das es uns aufgrund der unterstützten Konzepte bzw. aufgrund des gewählten Modellierungsparadigmas ermöglicht, den Algorithmus umzusetzen, auszuführen und zu testen. 
### Implementierung und Test

Die Lösung wird mit entsprechenden Werkzeugen schrittweise implementiert. Die Implementierung wird immer wieder ausgeführt, getestet und modifiziert, solange bis die Lösung fertig ist. Im Rahmen der Modifikation kann / wird es zu Anpassungen der Problemdefinition (Punkt 1) sowie des Algorithmus (Punkt 2) kommen, was zu weitern Zyklen führt. Die Lösung soll außerdem so weit wie möglich generalisiert werden, d.h. sie soll eine Klasse von Problemen und nicht nur ein spezifisches Problem mit bestimmten spezifischen Daten lösen. 

Wir beginnen mit der Implementierung des Programms mithilfe des gewählten Werkzeugeus (bestimmte Programmiersprache, bestimmte Entwicklungsumgebun). In kurzen Zyklen werden wir nach jeder kurzen Programmiertätigkeit immer wieder das Programm versuchen auszuführen. 

Wenn sich das Programm nicht starten lässt, analysieren wir die Fehlermeldungen des Interpreters / Compilers und bessern Syntaxfehler aus. Wir müssen uns an die Syntax der gewählten Programmiersprache ganz genau halten, sonst versteht der Computer nicht, was er für uns tun soll. 

Wenn sich das Programm jedoch starten lässt, können wir kontrollieren, ob das Programm die richtigen (Teil-)Ergebnisse im Sinne unserer Lösungsspezifikation liefert. Dazu benötigen wir Techniken, die es uns ermöglichen in die Laufzeit eines Programmes hineinzuschauen bzw. Ergebnisse des Programmes anzuzeigen. 

Falls das Programm beim Ausführen noch keine korrekten Lösungen / Lösungsteile liefert haben wir es ggf. mit einem Bug zu tun, die Semantik passt nicht. Dann können Modifikation in der Problemanaylse, im Algorithmus oder auch in der Implementierung nötig werden (zyklische Natur). Eine Modifikation der Problemanalyse führt zu Modifikation des Algorithmus und der Implementierung. Eine Modifikation im Algorithmus führ zu einer Modifikation der Implementierung. Jedenfalls wird es also immer Modifikationen in der Implementierung brauchen, um den Bug zu beheben.

Wenn das Programm im Sinne Lösungsspezifikation korrekte Ergebnisse liefert, dann sind wir fertig. Handelt es sich nur um eine Teillösung, gehen wir zur Bearbeitung des nächsten Lösungsteils über. Ggf. müssen gegen Ende mehrere Lösungsteile miteinander verbunden werden, um zur Gesamtlösung zu kommen.
### Referenzen zum Thema Computational Thinking

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