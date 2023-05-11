import random, time

anzahlDurchlauefe = int(input("Wieviele Durchläufe möchtest du spielen!"))
dauerDurchlauf = int(input("Wieviele Sekunden soll ein Durchlauf dauern?"))

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
laengeAlphabet = len(alphabet)

durchlauf = 1

while durchlauf <= anzahlDurchlauefe:
    zufallszahl = random.randint(0, laengeAlphabet-1)
    print("-----------------------")
    print("Runde " + str(durchlauf))
    print("Buchstabe: " + str(alphabet[zufallszahl]))
    vergangeneSekunden = 0
    print("*"*dauerDurchlauf)
    while vergangeneSekunden < dauerDurchlauf:
        time.sleep(1)
        print('>', flush="True", end="")
        vergangeneSekunden = vergangeneSekunden + 1
    print("")
    input("Durchlauf beendet. Nächster Durchlauf mit Enter")
    durchlauf = durchlauf + 1
print("Danke für's Spielen!")