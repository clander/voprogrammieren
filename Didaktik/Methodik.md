# Methodik

## Methodische Grundprinzipien
Für den Unterricht sind neben der Problemorientierung und der informatischen Modellbildung und Simulation u. A. folgende methodisch-didaktischen Ideen relevant:

* Standardablauf nach [Gagné](https://www.niu.edu/citl/resources/guides/instructional-guide/gagnes-nine-events-of-instruction.shtml).
  1. Aufmerksamkeit erregen
  2. Ziele bekannt geben
  3. Vorwissen aktivieren
  4. Input (Konzepte + Werkzeuge)
  5. Lerngerüste
  6. Übungsphasen
  7. Feedback
  8. Kompetenzcheck
  9. Transfer einüben
* Cognitive Apprenticeship
  * Authentische Problemstellungen in verschiedenen Kontexten
  * Lernen am Modell
  * Lerngerüste (und deren Ausblenden)
  * Einüben von Transfer (etwa durch Analogiebildung)
  * Reflexion, Artikulation, Exploration
* Transferlernen mit 3 - 4 Beispielen (siehe unten), die sich in der Tiefenstruktur ähneln, in der Oberlächenstruktur jedoch deutlich unterscheiden (unterschiedlicher Kontext):
  * Modelling Example (Tutorial, Videotraining)
  * Completion Example (Teile der Modellkette einer Iteration werden ausgelassen)
  * Conventional Example (alles wird durch die Lernenden erledigt, Lehrer ist Coach)
  * Transfer und Exploration
* Kontext vs. Abstraktion: Vom Abstrakten zum Konkreten und wieder zum Abstrakten (Kontextualisierung vs. Abstraktion); Explikation von Verhältnis zwischen Konzept, realisierendem Werkzeug und Anwendung im Rahmen der Problemlösung explizieren
* Genetischer Ansatz: Hinweis auf historische Relevanz / Genese der Inhalte
* Spiralprinzip (immer wieder Aufgreifen derselben Konzepte in höheren Komplexitätsstufen) und damit:
    * multiple (d.h. symbolische, ikonische und enaktive) Repräsentationen
    * vorwegnehmendes Lernen
    * Fortsetzbarkeit auf immer komplexeren Niveaus
* ... usw ...

## Problembasierter Unterricht mit Modelling - Completion - Conventional
1. Modelling-Example
   1. Problemstellung suchen:
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
        - [Open Roberta Lab](https://www.roberta-home.de/lab/)
        - siehe Übungsmaterial im Rahmen der verschiedenen [Werkzeuge-Webseiten](../Didaktik/Werkzeuge.md)
   2. Modelling Example 
      - Format: in Form eines 
         - Tutorial (Schritt für Schritt Anleitung, (siehe dazu auch das [Tamagotchi Tutorial aus der ersten Übung](../VO-Teil-1/GrundkonzepteProgrammierung/Tamagotchi/)
         - Videotraining (evtl. incl. H5P-Inhalten)
         - Lernaufgaben mit gelenktem entdeckendem Lernen
         - etc.
      - Inahlt: 
        - Fertige Anleitung zur Lösung der ersten Problemstellung.
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
2. Completion Example:
   - Das zweite Beispiel soll mit denselben Konzepten und Prozessen lösbar sein, jedoch eine völlig andere Fachdomäne betreffen. Es soll weniger Hilfestellungen beinhalten.
   - Art der Hilfestellung:
     - Problemanalyse incl. Lösungsansatz teilweise oder ganz gegeben
     - Algorithmus (grafisch oder als Pseudocode) teilweise oder ganz gegeben
     - Implementierung teilweise teilweise gegeben
   - Dieses Beispiel dient dem Einüben von Transfer.
3. Conventional Example:
   - wie zweite Problemstellung, jetzt jedoch ohne Hilfestllung.
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