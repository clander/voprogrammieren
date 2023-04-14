"""
--------------------------------------
Problemstellung: Body Mass Index (BMI)
--------------------------------------

...

Audience [V5]: Das Programmiererteam

Situation [V5]: zusätzlich zu [V5]: Das Programm soll besser strukturiert werden. Dadurch soll der Code übersichtlicher,
leichter wartbar, leichter anpassbar werden. Die Codequalität soll sich verbessern, die Funktionalität soll die gleiche bleiben.

...

Standards [V5]:
- Das Programm wird durch den Einsatz von Funktionen ein wenig modularisiert werden. 
- Dadurch werden Teile des Programms wiederverwendbar und besser lesbar.

---------
Konzepte:
---------
V7
- Funktionen als Modularisierungstechnik

---------
Werkzeug:
---------
V7
- Funktionen in Python
- Funktionsparameter in Python
- Rückgabetypen in Python
- Type-Hints für die Bekanntmachung von Typen von Parametern und Variablen
"""

def bmiBerechnen(kg:float,m:float):
    return kg / m**2

def bmiInterpretieren(bmi:float)->str:
    interpretation = ""
    if bmi < 18.5: # If-Anweisung mit Bedingung in Form eines logischen Ausdrucks mit Kleiner-Operator
        interpretation = "Untergewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung oben zutrifft
    elif bmi < 25: # Else-If: zweite Bedingung wird geprüft falls vorherige nicht zutrifft
        interpretation = "Normalgewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung geprüft wird und zutrifft
    elif bmi < 30: # Else-If: zweite Bedingung wird geprüft falls vorherige nicht zutrifft
        interpretation = "Übergewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung geprüft wird und zutrifft
    else: # Else: falls alle vorhergehenden Bedingungen nicht zutreffen werden nachfolgend eingerückte Anweisungen ausgeführt
        interpretation = "Adipositas"
    return interpretation

wiederholung = True # Bool'sche Schaltervariable

while wiederholung == True:
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
    bmi = bmiBerechnen(kilogramm,meter)
    ## Runden auf 2 Stellen
    bmiGerundet = round(bmi,2) # Runden-Funktion auf 2 Stellen
    ## Interpretation des Ergebnisses
    interpretation = bmiInterpretieren(bmi) # Variable für das Interpretationsergebnis mit vorerst leerem String

    #(A)usgabe
    print("Der berechnete BMI beträgt " + str(bmiGerundet) + " --> " + interpretation) # String-Konkatenation und String-Konvertierung
    #print(f"Der berechnete BMI beträgt {bmiGerundet} --> {interpretation}") # Alternative Ausgabe mit Format-String
    #print("Der berechnete BMI beträgt {:.2f} --> {}".format(bmi, interpretation)) # Alternative Ausgabe mit format-Funktion

    # Weitere Berechnung oder Programm beenden?
    eingabeWeitereBerechnung = input("Möchten Sie das Programm beenden? J oder j für Ja! ")
    if eingabeWeitereBerechnung.capitalize() == "J": # Methoden-Aufruf an String-Objekt, Logischer Ausdruck
        wiederholung = False

print("Vielen Dank, dass Sie unser Programm verwendet haben. Auf wiedersehen!")