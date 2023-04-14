import random

print("*** Schere, Stein, Papier ***")

optionen = ("Schere", "Stein", "Papier", "Exit") #Tuple, unveränderlich

playerwins = 0
computerwins = 0

while True:
    spielerwahl = input("Was wählst du? Tippe ein: [Schere]  [Stein]  [Papier]  [Exit] ")
    
    if spielerwahl not in optionen:
        print("--> Es stehen nur folgende Optionen zur Verfügung: [Schere]  [Stein]  [Papier]  [Exit] ")
        continue
    elif spielerwahl == "Exit":
        break
    else:
        computerwahl = optionen[random.randint(0,2)]
        print("--> Spielerwahl " + spielerwahl)
        print("--> Computerwahl " + computerwahl)
        if(spielerwahl == computerwahl):
            print("--> Unentschieden")
        elif(spielerwahl == "Schere" and computerwahl == "Papier"):
            print("--> Spieler gewinnt!")
            playerwins = playerwins + 1
        elif(spielerwahl == "Stein" and computerwahl == "Schere"):
            print("--> Spieler gewinnt!")
            playerwins = playerwins + 1
        elif(spielerwahl == "Papier" and computerwahl == "Stein"):
            print("--> Spieler gewinnt!")
            playerwins = playerwins + 1
        else:
            print("--> Computer gewinnt!")
            computerwins = computerwins + 1

print("*** Statistik ***")

print("- Playerwins: {0:d} Computerwins: {0:d}".format(playerwins,computerwins))

if playerwins > computerwins:
    print("- Spieler gewinnt!")
elif computerwins > playerwins:
    print("- Computer gewinnt!")
else:
    print("- Unentschieden!")