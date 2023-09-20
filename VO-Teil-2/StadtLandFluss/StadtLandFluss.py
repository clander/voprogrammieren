import random, time

anzahlDurchlauefe = int(input("Wieviele Durchläufe möchtest du spielen!"))
dauerDurchlauf = int(input("Wieviele Sekunden soll ein Durchlauf dauern?"))

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
laengeAlphabet = len(alphabet)

durchlauf = 1 

def wartenMitPfeil(sekunden):
    vergangeneSekunden = 1
    while vergangeneSekunden <= sekunden:
        time.sleep(1)
        print(vergangeneSekunden*'>')
        vergangeneSekunden = vergangeneSekunden + 1

def durchlaufStarten():
    zufallszahl = random.randint(0, laengeAlphabet-1)
    print("-----------------------")
    print("Runde " + str(durchlauf))
    print("Buchstabe: " + str(alphabet[zufallszahl]))
    wartenMitPfeil(dauerDurchlauf)

while durchlauf <= anzahlDurchlauefe:
    durchlaufStarten()
    durchlauf = durchlauf + 1
    input("Durchlauf beendet. Nächster Durchlauf mit Enter")

print("Danke für's Spielen!")