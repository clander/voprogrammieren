"""
=============
BMI VERSION 0
=============
---------
Standards
---------
- Formel für den BMI gefunden
- Interpretation für BMI gefunden
- Formel an einigen plausiblen Beispielwerten angewendet
- Python verwendet um einige BMIs zu berechnen und das Ergebnis auszugeben.

--------
Konzepte
--------
- Quellcode
- Kommentare
- Ausgeführter Programmcode
- Debugging
- REPL-Konsolen (Read-Evaluate-Print-Loop)
- Ausdrücke (Expressions - https://docs.python.org/3/reference/expressions.html)
- Anweisungen (Statements - https://docs.python.org/3/reference/simple_stmts.html)
- Sequenz von Anweisungen
- Funktionsaufrufe mit Parametern
- Abstraktion (unwesentliche Details weglassen)

---------
Werkzeuge
---------
- Einzeilige Kommenatare in Python mit #
- Mehrzeilige Kommentare in Pyhton mit Multiline-Strings (3 Anführungszeichen)
- Thonny-IDE
- Quellcode mit Thonny schreiben
- Quellcode mit Thonny ausführen
- Quellcode mit Thonny schrittweise ausführen / debuggen
- Interaktive REPL-Python-Konsole mit Thonny
- Arithmetische Ausdrücke in Python
- Anweisungen in Python
- Anweisungssequenzen in Python
- Print-Funktion mit Parameter verwenden
"""


"""
Recherchergebnis entsprechend den Ausführung in https://de.wikipedia.org/wiki/Body-Mass-Index.

Der Body-Mass-Index wird folgendermaßen berechnet:

    BMI = Masse (in kg) / Groesse (in Meter zum Quadrat)

Der BMI wird also in der Maßeinheit kg pro m² angegeben.

Der BMI wird von Versicherungen verwendet.
Der BMI wird im Fitness-Bereich verwendet.
Der BMI wird im Bereich der Ernährungsberatung verwendet.
Der BMI wird in der Model-Szene verwendet.

Der BMI weißt für Frauen und Männer leicht unterschiedliche Werte auf.

Interpretation (im Groben):

Untergewicht: < 18,5
Normalgewicht: < 25
Übergewicht: < 30
Adipositas: >= 30

"""

70 / 1.85**2 # Expression-Statement ohne Effekt (-> Expression-Statements primär in REPL sinnvoll)
print(90 / 1.85**2) # Arithmetischer Ausdruck + Print-Funktionsaufruf mit Ergebnis dieses Ausdrucks
print(80 / 1.85**2) # Sequenz: jede weitere Anweisung kommt in eine neue Zeile (Achtung auf die Einrückungen)
print(70 / 1.55**2) # ...
print(70 / 1.85**2) # ...