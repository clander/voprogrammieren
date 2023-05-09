"""
=============
BMI VERSION 5
=============

---------
Standards
---------
- Fertiges Python-Programm mit folgenden Aspekten zusätzlich zu [V4]:
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
    if bmi < 18.5:
        interpretation = "Untergewicht"
    elif bmi < 25:
        interpretation = "Normalgewicht"
    elif bmi < 30:
        interpretation = "Übergewicht"
    else:
        interpretation = "Adipositas"
    return interpretation

variante = input("1) BMI für eine Eingabe berechnen 2) BMIs für eine Messreihe berechnen ")
if variante == "1":
    wiederholung = True

    while wiederholung == True:
        print("************ BMI-Berechnung ************")
        eingabeErfolgreich = False
        while(not eingabeErfolgreich):
            eingabeKilogramm = input("Bitte geben Sie ihr Gewicht in Kilogramm an (Komma als Punkt): ")
            eingabeMeter = input("Bitte geben Sie ihre Größe in Meter an (Komma als Punkt angeben): ")
            try:
                kilogramm = float(eingabeKilogramm)
                meter = float(eingabeMeter)
                eingabeErfolgreich = True
            except:
                print("Bitte nur Zahlen eingeben!")
                eingabeErfolgreich = False
        bmi = bmiBerechnen(kilogramm,meter)
        bmiGerundet = round(bmi,2)
        interpretation = bmiInterpretieren(bmi)
        ausgabe = "Der berechnete BMI beträgt " + str(bmiGerundet) + " --> " + interpretation
        print(ausgabe)
        eingabeWeitereBerechnung = input("Möchten Sie das Programm beenden? J oder j für Ja! ")
        if eingabeWeitereBerechnung.capitalize() == "J":
            wiederholung = False
    print("Vielen Dank, dass Sie unser Programm verwendet haben. Auf wiedersehen!")
elif variante == "2":
    messreihe = []
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
            interpretation = ""
            if bmi < 18.5:
                interpretation = "Untergewicht"
            elif bmi < 25:
                interpretation = "Normalgewicht"
            elif bmi < 30:
                interpretation = "Übergewicht"
            else:
                interpretation = "Adipositas"
            print("BMI für eine Masse von " + str(kg) + "kg und eine Größe von + " + str(m) + " m beträgt " + str(bmiGerundet) + " --> " + str(interpretation))
            i = i + 2
else:
    print("Bitte nur 1 oder 2 angeben!")
