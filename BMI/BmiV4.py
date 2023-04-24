"""
=============
BMI VERSION 4
=============

---------
Standards
---------
- Fertiges Python-Programm mit folgenden Aspekten zusätzlich zu [V3]:
- Benutzer wird über Falscheingaben (Zahlen) informiert und bekommt solange die Möglichkeit alles neu einzugeben, bis alles passt.
- Wiederholte Berechnung ermöglichen, wenn der Benutzer nach einer Berechnung J eingibt.

--------
Konzepte
--------
- Wiederholung
- Bool'sche Schalter-Variablen

---------
Werkzeuge
---------
- While-Loop in Python
- Bool'sche Variablen in Python

"""

wiederholung = True #Bool'sche Schaltervariable

while wiederholung == True:
    print("************ BMI-Berechnung ************")
    #(E)ingabe
    eingabeErfolgreich = False # Boo'sche Schaltervariable
    while not eingabeErfolgreich:
        eingabeKilogramm = input("Bitte geben Sie ihr Gewicht in Kilogramm an (Komma als Punkt): ") #Input-Funktion mit Parameter und String-Rückgabe
        eingabeMeter = input("Bitte geben Sie ihre Größe in Meter an (Komma als Punkt angeben): ")
        try:
            kilogramm = float(eingabeKilogramm)
            meter = float(eingabeMeter)
            if kilogramm >= 0 and meter >= 0:
                eingabeErfolgreich = True
            else:
                print("Bitte nur positive Zahlen eingeben!")
                eingabeErfolgreich = False
        except:
            print("Bitte nur Zahlen eingeben!")
            eingabeErfolgreich = False
  
    # (V)erarbeitung
    bmi = kilogramm / meter**2
    bmiGerundet = round(bmi,2) 
    interpretation = ""
    if bmi < 18.5: 
        interpretation = "Untergewicht" 
    elif bmi < 25: 
        interpretation = "Normalgewicht" 
    elif bmi < 30: 
        interpretation = "Übergewicht" 
    else: 
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