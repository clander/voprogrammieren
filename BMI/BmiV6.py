"""
=============
BMI VERSION 6
=============

---------
Standards
---------
- Fertiges Python-Programm mit folgenden Aspekten zusätzlich zu [V5]:
- Der Benutzer gibt eine Messreihe ein und bekommt für je zwei Eingaben einen BMI-Wert berechnet und ausgegeben.

--------
Konzepte
--------
- Wiederholung
- Datenstruktur Listen
- Arbeiten mit Listen - Iteration über Listen

--------
Werkzeug
--------
- While in Python
- Listen in Python

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

variante = input("1) BMI für eine Eingabe berechnen 2) BMIs für eine Messreihe berechnen ")

if variante == "1":
    wiederholung = True # Bool'sche Schaltervariable

    while wiederholung == True:
        print("************ BMI-Berechnung ************")
        #(E)ingabe
        eingabeErfolgreich = False # Boo'sche Schaltervariable
        while(not eingabeErfolgreich):
            eingabeKilogramm = input("Bitte geben Sie ihr Gewicht in Kilogramm an (Komma als Punkt): ") #Input-Funktion mit Parameter und String-Rückgabe
            eingabeMeter = input("Bitte geben Sie ihre Größe in Meter an (Komma als Punkt angeben): ")
            try:
                kilogramm = float(eingabeKilogramm)
                meter = float(eingabeMeter)
                eingabeErfolgreich = True
            except:
                print("Bitte nur Zahlen eingeben!")
                eingabeErfolgreich = False

        #(V)erarbeitung
        ## Berechnung
        bmi = bmiBerechnen(kilogramm,meter)
        ## Runden auf 2 Stellen
        bmiGerundet = round(bmi,2) # Runden-Funktion auf 2 Stellen -> Diskussion über Fließkommazahlen und Runden-Problematik
        ## Interpretation des Ergebnisses
        interpretation = bmiInterpretieren(bmi)

        #(A)usgabe
        print("Der berechnete BMI beträgt " + str(bmiGerundet) + " --> " + interpretation) # String-Konkatenation und String-Konvertierung
        #print(f"Der berechnete BMI beträgt {bmiGerundet} --> {interpretation}") # Alternative Ausgabe mit Format-String
        #print("Der berechnete BMI beträgt {:.2f} --> {}".format(bmi, interpretation)) # Alternative Ausgabe mit format-Funktion

         # Weitere Berechnung oder Programm beenden?
        eingabeWeitereBerechnung = input("Möchten Sie das Programm beenden? J oder j für Ja! ")
        if eingabeWeitereBerechnung.capitalize() == "J": # Methoden-Aufruf an String-Objekt, Logischer Ausdruck
            wiederholung = False

    print("Vielen Dank, dass Sie unser Programm verwendet haben. Auf wiedersehen!")

elif variante == "2":
    messreihe = [] # Liste anlegen
    print("Bitte geben Sie die Messreihe ein!")
    while True:
        eingabe = input()
        if eingabe == "#":
            break
        else:
            eingabeErfolgreich = False
            while not eingabeErfolgreich:
                try:
                    umwandlungZahl = float(eingabe)
                    if umwandlungZahl >= 0:
                        eingabeErfolgreich = True
                        messreihe.append(umwandlungZahl)
                    else:
                        print("Bitte nur positive Zahlen eingeben!")
                        eingabe = input()
                except:
                    print("Bitte nur Zahlen eingeben!")
                    eingabe = input()
    if len(messreihe) % 2 != 0:
        print("Sie müssen immer je zwei Werte eingeben, einen für die Masse in kg und einen für die Grösse in m")
    else:
        i = 0
        while i < len(messreihe)-1:
            kg = messreihe[i]
            m = messreihe[i+1]
            bmi = kg / m**2
            bmiGerundet = round(bmi,2)
            interpretation = "" # Variable für das Interpretationsergebnis mit vorerst leerem String
            if bmi < 18.5: # If-Anweisung mit Bedingung in Form eines logischen Ausdrucks mit Kleiner-Operator
                interpretation = "Untergewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung oben zutrifft
            elif bmi < 25: # Else-If: zweite Bedingung wird geprüft falls vorherige nicht zutrifft
                interpretation = "Normalgewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung geprüft wird und zutrifft
            elif bmi < 30: # Else-If: zweite Bedingung wird geprüft falls vorherige nicht zutrifft
                interpretation = "Übergewicht" # Bedingte Anweisung, eingerückt, wird ausgeführt, wenn Bedingung geprüft wird und zutrifft
            else: # Else: falls alle vorhergehenden Bedingungen nicht zutreffen werden nachfolgend eingerückte Anweisungen ausgeführt
                interpretation = "Adipositas"
            print(f"BMI für eine Masse von {kg} kg und eine Größe von {m} m beträgt {bmiGerundet} --> {interpretation}")
            i = i + 2;
else:
    print("Bitte nur 1 oder 2 angeben!")
