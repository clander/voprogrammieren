import random
import time

anzahlDurchlaeufeEingabe = input("Wieviele Durchläufe möchtest du spielen? ")
anzahlDurchlaeufe = int(anzahlDurchlaeufeEingabe);
dauerDurchlaufEingabe = input("Wieviele Sekunden soll ein Durchlauf dauern? ")
dauerDurchlauf = int(dauerDurchlaufEingabe);

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
laenge = len(alphabet)

durchlaufnummer = 1

while durchlaufnummer <= anzahlDurchlaeufe:
    zufallszahl = random.randint(0,laenge-1)
    print("--------------------------------")
    print("Runde " + str(durchlaufnummer))
    print("Der Buchstabe von Runde " + str(durchlaufnummer) + " ist: "+ str(alphabet[zufallszahl]))
    vergangeneSekunden = 0
    while vergangeneSekunden < dauerDurchlauf:
        time.sleep(1)
        t1 = time.time()
        print('>', flush="True", end='')
        vergangeneSekunden = vergangeneSekunden + 1
    input("\nDurchlauf für Buchstaben " + alphabet[zufallszahl] + " ist beendet! Weiter mit einer beliebigen Taste ...  ")
    durchlaufnummer = durchlaufnummer + 1
print("Danke dass du mit mir gespielt hast. Bis bald!")