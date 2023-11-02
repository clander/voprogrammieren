ende = False
temperaturen = []
summe = 0

print("Bitte Temperaturdaten eingeben (Ende der Eingabe mit x)")

while not ende:
    eingabe = input()
    if(eingabe=='x'):
        ende = True
    else:
        try:
            temperaturwert = int(eingabe)
            temperaturen.append(temperaturwert)
        except:
            print("Bitte nur Zahlen eingeben!")

for i in temperaturen:
    summe = summe + i
print(f"Summe: {summe}")

mittelwert = summe / len(temperaturen)
print(f"Mittelwert: {mittelwert}")
