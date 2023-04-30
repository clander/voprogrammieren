"""
=============
BMI VERSION 3
=============

---------
Standards
---------
- Fertiges Python-Programm mit folgenden Aspekten zusätzlich zu [V2]
- Ausgabe des Interpretationsergebnisses

---------
Konzepte
---------
- Alternative
- Bedingung in Form eines logischen Ausdrucks
- Bedingungs-Ergebnis in Form von Bool'schen Werten

---------
Werkzeug
---------
- Logische Ausdrücke in Python
- Bool'sche Ergebnisse in Python
- Logische Operatoren in Python
- If in Python
- Else-If in Python

"""

print('************ BMI-Berechnung ************')
eingabeKilogramm = input('Bitte geben Sie ihr Gewicht in Kilogramm an: ')
eingabeMeter = input('Bitte geben Sie ihre Größe in Meter an: ')
kilogramm = float(eingabeKilogramm)
meter = float(eingabeMeter)
bmi = kilogramm / (meter * meter)
bmiGerundet = round(bmi, 2)
interpretation = ""
if bmi < 18:
    interpretation = "Untergewicht"
if bmi >=18 and bmi < 26:
    interpretation = "Normalgewicht"
if bmi >=26 and bmi < 31:
    interpretation = "Übergewicht"
if bmi >= 31:
    interpretation = "Adipositas"
"""
# Folgende IF-Anweisung ist eine elegantere Variante von oben:
if bmi < 18:
    interpretation = "Untergewicht"
elif bmi < 26:
    interpretation = "Normalgewicht"
elif bmi < 31:
    interpretation = "Übergewicht"
else:
    interpretation = "Adipositas"
"""
print("Der berechnete BMI beträgt " + str(bmiGerundet) + " --> " + interpretation)
