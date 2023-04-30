"""
=============
BMI VERSION 1
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
print('************ BMI-Berechnung ************')
eingabeKilogramm = input('Bitte geben Sie ihr Gewicht in Kilogramm an: ')
eingabeMeter = input('Bitte geben Sie ihre Größe in Meter an: ')
kilogramm = float(eingabeKilogramm)
meter = float(eingabeMeter)
bmi = kilogramm / (meter * meter)
bmiGerundet = round(bmi, 2)
print('Der berechnete BMI beträgt ' + str(bmiGerundet))