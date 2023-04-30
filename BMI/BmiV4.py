"""
=============
BMI VERSION 4
=============

---------
Standards
---------
- Das Programm wird durch den Einsatz von Funktionen ein wenig modularisiert werden. 
- Dadurch werden Teile des Programms wiederverwendbar und besser lesbar.

--------
Konzepte
--------
- Funktionen als Modularisierungstechnik

---------
Werkzeuge
---------
- Funktionen in Python
- Funktionsparameter in Python
- Rückgabetypen in Python
- Type-Hints für die Bekanntmachung von Typen von Parametern und Variablen
"""

def bmiBerechnen(kg:float,m:float):
    return kg / m**2
def bmiInterpretieren(bmi:float)->str:
    interpretation = ""
    if bmi < 18.5:
        interpretation = "Untergewicht" 
    elif bmi < 25: 
        interpretation = "Normalgewicht"  
    elif bmi < 30: 
        interpretation = "Übergewicht" 
    else:
        interpretation = "Adipositas"
    return interpretation
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
    bmi = bmiBerechnen(kilogramm,meter)
    bmiGerundet = round(bmi,2)
    interpretation = bmiInterpretieren(bmi)
    ausgabe = "Der berechnete BMI beträgt " + str(bmiGerundet) + " --> " + interpretation
    print(ausgabe)
    eingabeWeitereBerechnung = input("Möchten Sie das Programm beenden? J oder j für Ja! ")
    if eingabeWeitereBerechnung.capitalize() == "J": # Methoden-Aufruf an String-Objekt, Logischer Ausdruck
        wiederholung = False
print("Vielen Dank, dass Sie unser Programm verwendet haben. Auf wiedersehen!")