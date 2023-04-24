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
    print(f"Der Buchstabe von Runde \033[96m{durchlaufnummer}\033[0m ist: \033[96m {alphabet[zufallszahl]}\033[0m")
    vergangeneSekunden = 0
    t0 = time.time()
    while vergangeneSekunden < dauerDurchlauf:
        print("\a.", end="")#\a. spielt einen Beep per Standard-Out, danach folgt der Punkt und damit kein Absatzzeichen gemacht wird, endet die Ausgabe mit dem leeren String
        time.sleep(1)
        t1 = time.time()
        vergangeneSekunden = t1-t0
    input("\nDurchlauf beendet! Weiter mit einer beliebigen Taste ...  ")
    durchlaufnummer = durchlaufnummer + 1
print("Danke dass du mit mir gespielt hast. Bis bald!")
