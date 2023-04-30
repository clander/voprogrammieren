"""
=============
BMI VERSION 3
=============

---------
Standards
---------
- Fertiges Python-Programm mit folgenden Aspekten zusätzlich zu [V2]:
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
wiederholung = True
while wiederholung == True:
    print("************ BMI-Berechnung ************")
    eingabeErfolgreich = False
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
    ausgabe = "Der berechnete BMI beträgt " + str(bmiGerundet) + " --> " + interpretation
    print(ausgabe)
    eingabeWeitereBerechnung = input("Möchten Sie das Programm beenden? J oder j für Ja! ")
    if eingabeWeitereBerechnung.capitalize() == "J":
        wiederholung = False

print("Vielen Dank, dass Sie unser Programm verwendet haben. Auf wiedersehen!")