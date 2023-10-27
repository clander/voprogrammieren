import tkinter as tk
from tkinter import messagebox

def bmiRechnenUndInterpretieren():
    kg = float(kgTextBinding.get())
    m = float(mTextBinding.get())
    bmi = kg / (m * m)
    messagebox.showinfo(title="BMI", message=f"Dein BMI beträgt {bmi}")

root = tk.Tk() # Hauptfenster
root.title("BMI Berechnung") #Title

labelKg = tk.Label(root,text="Gewicht in kg:")
labelKg.grid(row=0,column=0)

kgTextBinding = tk.StringVar()
inputKg = tk.Entry(root,textvariable=kgTextBinding)
inputKg.focus()
inputKg.grid(row=0,column=1)

labelM = tk.Label(root,text="Gröesse in m:")
labelM.grid(row=1,column=0)

mTextBinding = tk.StringVar()
inputM = tk.Entry(root,textvariable=mTextBinding)
inputM.grid(row=1,column=1)

btnBMIRechnen = tk.Button(root, text="BMI rechnen", command=bmiRechnenUndInterpretieren)
btnBMIRechnen.grid(row=5,columnspan=2)

btnQuit = tk.Button(root, text="Beenden", command=quit)
btnQuit.grid(row=6,columnspan=2)