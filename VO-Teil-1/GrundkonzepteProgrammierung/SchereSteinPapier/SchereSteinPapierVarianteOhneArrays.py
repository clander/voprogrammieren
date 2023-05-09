import random
print("*** Schere, Stein, Papier ***")
spielerGewinne = 0
computerGewinne = 0
while True:
    spielerwahl = input("Was wählst du? Tippe ein: [Schere]  [Stein]  [Papier]  [Exit] ")
    if spielerwahl != "Schere" and spielerwahl != "Stein" and spielerwahl != "Papier" and spielerwahl != "Exit":
        print("Es stehen nur folgende Optionen zur Verfügung: [Schere]  [Stein]  [Papier]  [Exit] ")
        continue
    elif spielerwahl == "Exit":
        break
    else:
        zufallszahl = random.randint(0,2)
        if zufallszahl == 0:
            computerwahl = "Schere"
        elif zufallszahl == 1:
            computerwahl = "Stein"
        elif zufallszahl == 2:
            computerwahl = "Papier"
        print("[Spielerwahl] : " + spielerwahl)
        print("[Computerwahl] : " + computerwahl)
        if spielerwahl == computerwahl:
            print(">Unentschieden")
        elif spielerwahl == "Schere" and computerwahl == "Papier":
            print(">Spieler gewinnt")
            spielerGewinne = spielerGewinne + 1
        elif spielerwahl == "Stein" and computerwahl == "Schere":
            print(">Spieler gewinnt")
            spielerGewinne = spielerGewinne + 1
        elif spielerwahl == "Papier" and computerwahl == "Stein":
            print(">Spieler gewinnt")
            spielerGewinne = spielerGewinne + 1
        else:
            print(">Computer gewinnt")
            computerGewinne = computerGewinne + 1
print("")
print("*************** Statistik ***************")
print(str(spielerGewinne) + " (Spieler) : " + str(computerGewinne) + " (Computer)")
if spielerGewinne > computerGewinne:
    print("Spieler gewinnt das Match")
elif computerGewinne > spielerGewinne:
    print("Computer gewinnt das Match")
else:
    print("Das Match geht untentschieden aus!")
print("*****************************************")