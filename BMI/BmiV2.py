"""
=============
BMI VERSION 2
=============

---------
Standards
---------
- Programm fragt kg und m vom Benutzer ab
- Programm berechnte BMI korrekt
- Programm gibt Berechnungsergebnis gerundet aus

--------
Konzepte
--------
- Problemlösungszyklus beim Programmieren
- EVA-Prinzip
- User-Interfaces
- Funktionsaufrufe mit Rückgabewerten
- Variablen
- Datentypen
- Zuweisung
- Generalisierung (Verallgemeinerung einer spezifischen Berechnung zu einem allgemeingültigen Berechnungsmodell)
- Abstraktion (Im Sinne des zu entwickelnden System wichtige Elemente identifizieren, Rest weglassen)

---------
Werkzeuge
---------
- Zyklus: Code schreiben - Syntaxfehler beheben - Code ausführen - Funktionalität verbessern und Bugs beheben - Fertiges Programm
- Input-Funktion mit Parametern
- Print-Funktion mit Stringinterpolation und String-Konkatenation
- Variablen in Python
- Zuweisungsoperation in Python
- Wichtige Datentypen für Zahlen und Text in Python
- Type-Funktion
- Typumwandlung mit Konstruktorfunktionen
- String-Konkatenation

"""

print("************ BMI-Berechnung ************")
#(E)ingabe
eingabeKilogramm = input("Bitte geben Sie ihr Gewicht in Kilogramm an: ") #Variable, Zuweisung, Input-Funktion mit Parameter und String-Rückgabe
eingabeMeter = input("Bitte geben Sie ihre Größe in Meter an (Komma als Punkt angeben!): ")
#print(type(eingabeKilogramm)) # so kann man den Typ der Eingabe sehen


#(V)erarbeitung
## Typkonvertierung
kilogramm = float(eingabeKilogramm) # Variable, Zuweisung, Funktionsaufruf mit Rückgabewert
meter = float(eingabeMeter)
## Berechnung
bmi = kilogramm / meter**2 # Variable, Zuweisung, Arithmetischer Ausdruck
## Runden auf 2 Stellen
bmiGerundet = round(bmi,2) # Variable, Zuweisung, Runden-Funktion auf 2 Stellen -> Diskussion über Fließkommazahlen und Runden-Problematik


#(A)usgabe
print("Der berechnete BMI beträgt " + str(bmiGerundet)) # String-Konkatenation und String-Konvertierung
#print(f"Der berechnete BMI beträgt {bmiGerundet}") # Alternative Ausgabe mit Format-String
#print("Der berechnete BMI beträgt {:.2f}".format(bmi)) # Alternative Ausgabe mit format-Funktion
