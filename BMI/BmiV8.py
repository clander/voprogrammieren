"""
--------------------------------------
Problemstellung: Body Mass Index (BMI)
--------------------------------------

...

Audience [V8]: Die Benutzer

Situation [V8]: zusätzlich zu [V5]: Das Programm soll mit einer grafischen Benutzeroberfläche ausgestattet werden. 
...

Standards [V8]:
- Das Programm kann vollständig über eine grafische Benutzeroberfläche bedient werden.

---------
Konzepte:
---------
V8
- GUIs mit Widgets,
- Layout,
- Events,
- Databinding

---------
Werkzeug:
---------
V8
- tkinter GUI-Bibliothek mit
- Labels
- Buttons
- Textfields
- MessageBox
- StringVars für Textbinding
- Gridlayout
"""

import tkinter as tk
from tkinter import messagebox

def bmiRechnenUndInterpretieren():
    try:
        kg = float(kgTextBinding.get())
        m = float(mTextBinding.get())
        bmi = kg / m**m
        ergebnisTextBinding.set(str(round(bmi,2)))
        if bmi <= 18:
            interpretation = "Untergewicht"
        elif bmi <= 25:
            interpretation = "Normalgewicht"
        elif bmi <= 29:
            interpretation = "Übergewicht"
        else:
            interpretation = "Adipositas"
        ergebnisInterpretationBinding.set(interpretation)
    except:
        messagebox.showerror(title="Falscheingabe", message="Bitte Zahlen eingeben!")

# Hauptprogramm

root = tk.Tk() # Hauptfenster
root.title("BMI Berechnung") # Title Hauptfenster

#Eingabe für kg
labelKg = tk.Label(root,text="Gewicht in kg:")
labelKg.grid(row=0,column=0)
kgTextBinding = tk.StringVar()
inputKg = tk.Entry(root,textvariable=kgTextBinding)
inputKg.focus()
inputKg.grid(row=0,column=1)

#Eingabe für m
labelM = tk.Label(root,text="Grösse in m:")
labelM.grid(row=1,column=0)
mTextBinding = tk.StringVar()
inputM = tk.Entry(root,textvariable=mTextBinding)
inputM.grid(row=1,column=1)

#Ergebnis-Label
ergebnisTextBinding = tk.StringVar()
ergebnisTextBinding.set("Ergebnis:")
lblBmiErgebnis = tk.Label(root, textvariable=ergebnisTextBinding)
lblBmiErgebnis.grid(row=2,columnspan=2)

#Interpretation-Label
ergebnisInterpretationBinding = tk.StringVar()
ergebnisInterpretationBinding.set("Interpretation:")
lblInterpretation = tk.Label(root, textvariable=ergebnisInterpretationBinding)
lblInterpretation.grid(row=3,columnspan=2)

#Button
btnBerechnen = tk.Button(root, text="BMI berechnen", command=bmiRechnenUndInterpretieren)
btnBerechnen.grid(row=4,columnspan=2)

#Button
btnBerechnen = tk.Button(root, text="Beenden", command=quit)
btnBerechnen.grid(row=5,columnspan=2)

root.mainloop()