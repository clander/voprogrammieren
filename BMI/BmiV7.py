"""
=============
BMI VERSION 7
=============

---------
Standards
---------
- Das Programm wird durch den Einsatz von Funktionen noch stärker modularisiert.
- Insbesondere werden neben den aus V5 bereits vorhandenen Funktionen 
  für die Berechnung und die Interpretation des BMI auch Funktionen für die Eingabeverarbeitung bereitgestellt.


--------
Konzepte
--------
- Weitere Funktionen als Modularisierungstechnik

--------
Werkzeug
--------
- Funktionen in Python
- Funktionsparameter in Python
- Rückgabetypen in Python
- Type-Hints für die Bekanntmachung von Typen von Parametern und Variablen
"""

# Funktionen

def bmiBerechnen(kg,m):
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

def istPositiveKommazahl(numberString:str)->bool:
    try:
        if float(numberString) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

def eingabePositiveKommazahl(label:str)->float:
    while True:
        eingabe = input(label)
        if not istPositiveKommazahl(eingabe):
            print("-> Eingabe muss eine positive Kommazahl sein!")
            continue
        else:
            return float(eingabe)

def messreiheEinlesen() -> list[float]:
    messreihe = [] # type: list[float]
    print("-> Bitte geben Sie die Werte ein!")
    while True:
        eingabe = input()
        if eingabe == "#":
            if len(messreihe) < 2 or len(messreihe) % 2 != 0:
                print("-> Sie müssen eine gerade Anzahl von Zaheln eingeben (immer je zwei Werte)!")
                continue
            else:
                return messreihe
        else:
            try:
                eingabeZahl = float(eingabe)
                if eingabeZahl >= 0:
                    messreihe.append(eingabeZahl)
                else:
                    print("-> Bitte nur positive Kommazahlen eingeben!")
            except ValueError:
                print("-> Bitte nur positive Kommazahlen eingeben!")

# Programm

ende = False

while not ende:
    
    print("************************************* MENÜ ************************************** ")
    variante = input("1) BMI für eine Eingabe berechnen 2) BMIs für eine Messreihe berechnen 3) Beenden ")

    if variante == "1":
        print("************** BMI-Einzelberechnung **************")
        kg = eingabePositiveKommazahl("-> Bitte geben Sie ihr Gewicht in Kilogramm an: ")
        m = eingabePositiveKommazahl("-> Bitte geben Sie ihre Größe in Meter an (Komma als Punkt angeben!): ")
        bmi = bmiBerechnen(kg,m)
        interpretation = bmiInterpretieren(bmi)
        print("[Der berechnete BMI beträgt " + str(round(bmi,2)) + " --> " + interpretation + "]")
    elif variante == "2":
        print("************ BMI-Messreihenberechnung ************")
        messreihe = messreiheEinlesen()
        i = 0
        while i < len(messreihe)-1:
            kg = messreihe[i]
            m = messreihe[i+1]
            bmi = bmiBerechnen(kg,m)
            bmiGerundet = round(bmi,2)
            interpretation = bmiInterpretieren(bmi)
            print(f"[BMI für eine Masse von {kg} kg und eine Größe von {m} m beträgt {bmiGerundet} --> {interpretation}]")
            i = i + 2;
    elif variante == "3":
        ende = True
        print("-> Auf wiedersehen!")
    else:
        print("-> Bitte 1, 2 oder 3 wählen!")
