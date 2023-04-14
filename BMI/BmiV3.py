"""
--------------------------------------
Problemstellung: Body Mass Index (BMI)
--------------------------------------

Goal: Wir möchten den Benutzern unserer Fitnessgeräte die Möglichkeit geben, ihren BMI
schnell zu berechnen, bei Bedarf die Ergebnisse zu speichern und den Verlauf der BMI-Berechnungsergebnisse anzuzeigen.

Role: Du bist Programmierer im Unternehmen Fitness4All GmbH. 

Audience: Zielgruppe unserer Produkte sind die Benutzer unserer Fitness-Geräte.

Situation [V3]: Als Mitglied im Programmierteam wirst du damit beauftragt, ein Prorgramm zu schreiben, das den
Benutzer nach den Werten für die Berechnung des BMI fragt und das Berechnungsergebnis daraufhin ausgibt. Das
Programm soll außerdem den BMI interpretieren und auch das Interpretationsergebnis
(Untergewicht, Normalgewicht, Übergewicht, Adipositas) ausgeben.

Product [V3]: Als Produkt entwickelst du ein fertiges Python-Programm mit entsprechendem Userinterface.

Standards [V3]:
- Fertiges Python-Programm mit folgenden Aspekten zusätzlich zu [V2]
- Ausgabe des Interpretationsergebnisses

---------
Konzepte:
---------
V3
- Alternative
- Bedingung in Form eines logischen Ausdrucks
- Bedingungs-Ergebnis in Form von Bool'schen Werten

---------
Werkzeug:
---------
V3
- Logische Ausdrücke in Python
- Bool'sche Ergebnisse in Python
- Logische Operatoren in Python
- If in Python
- Else-If in Python

"""

print("************ BMI-Berechnung ************")
#(E)ingabe
eingabeKilogramm = input("Bitte geben Sie ihr Gewicht in Kilogramm an: ") #Input-Funktion mit Parameter und String-Rückgabe
eingabeMeter = input("Bitte geben Sie ihre Größe in Meter an (Komma als Punkt angeben!): ")
#print(type(eingabeKilogramm)) # so kann man den Typ der Eingabe sehen


#(V)erarbeitung
## Typkonvertierung
kilogramm = float(eingabeKilogramm)
meter = float(eingabeMeter)
## Berechnung
bmi = kilogramm / meter**2
## Runden auf 2 Stellen
bmiGerundet = round(bmi,2) # Runden-Funktion auf 2 Stellen -> Diskussion über Fließkommazahlen und Runden-Problematik
## Interpretation des Ergebnisses
interpretation = "" # Variable für das Interpretationsergebnis mit vorerst leerem String

if bmi < 18.5: # If-Anweisung mit Bedingung in Form eines logischen Ausdrucks mit Kleiner-Operator
    interpretation = "Untergewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung oben zutrifft
elif bmi < 25: # Else-If: zweite Bedingung wird geprüft falls vorherige nicht zutrifft
    interpretation = "Normalgewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung geprüft wird und zutrifft
elif bmi < 30: # Else-If: zweite Bedingung wird geprüft falls vorherige nicht zutrifft
    interpretation = "Übergewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung geprüft wird und zutrifft
else: # Else: falls alle vorhergehenden Bedingungen nicht zutreffen werden nachfolgend eingerückte Anweisungen ausgeführt
    interpretation = "Adipositas"

#(A)usgabe
print("Der berechnete BMI beträgt " + str(bmiGerundet) + " --> " + interpretation) # String-Konkatenation und String-Konvertierung
#print(f"Der berechnete BMI beträgt {bmiGerundet} --> {interpretation}") # Alternative Ausgabe mit Format-String
#print("Der berechnete BMI beträgt {:.2f} --> {}".format(bmi, interpretation)) # Alternative Ausgabe mit format-Funktion