"""
--------------------------------------
Problemstellung: Body Mass Index (BMI)
--------------------------------------

...

Situation [V4]: Als Mitglied im Programmierteam wirst du damit beauftragt, ein Programm zu schreiben, das den
Benutzer nach den Werten für die Berechnung des BMI fragt und das Berechnungsergebnis daraufhin ausgibt. Das
Programm soll außerdem den BMI interpretieren und auch das Interpretationsergebnis
(Untergewicht, Normalgewicht, Übergewicht, Adipositas) ausgeben. Der Benutzer soll mehrere Berechnungen durchführen können,
wenn er mit "J" bestätigt. In allen anderen Fällen soll das Programm beendet werden.

Product [V4]: Als Produkt entwickelst du ein fertiges Python-Programm mit entsprechendem Userinterface.

Standards [V4]:
- Fertiges Python-Programm mit folgenden Aspekten zusätzlich zu [V3]:
- Wiederholte Berechnung ermöglichen wenn der Benutzer nach einer Berechnung J eingibt.

---------
Konzepte:
---------
V4
- Wiederholung
- Bool'sche Schalter-Variablen

---------
Werkzeug:
---------
V4
- While-Loop in Python
- Bool'sche Variablen in Python

"""

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

    # Weitere Berechnung oder Programm beenden?
    eingabeWeitereBerechnung = input("Möchten Sie das Programm beenden? J oder j für Ja! ")
    if eingabeWeitereBerechnung.capitalize() == "J": # Methoden-Aufruf an String-Objekt, Logischer Ausdruck
        wiederholung = False

print("Vielen Dank, dass Sie unser Programm verwendet haben. Auf wiedersehen!")