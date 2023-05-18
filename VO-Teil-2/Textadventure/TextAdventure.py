import random, sys

rucksack = {
  "schluessel": False ,
  "schwert": False
}

def eingangshalle():
    print("*********************")
    print("*** Eingangshalle ***")
    print("*********************")
    while(True):
        eingabe = input("Was möchtest du tun? u) Raum untersuchen  n) Tür im Norden nutzen  s) Tür im Süden nutzen r) Rucksack öffnen ... ")
        if eingabe == "u":
            print("Du findest nichts.")
        elif eingabe == "n":
            if rucksack["schluessel"]:
                print("--> Du verwendest den Schlüssel und gehst durch die Tür im Norden")
                rittersaal()
                break
            else:
                print("Die Tür ist versperrt, du kommst da nicht durch!")
        elif eingabe == "s":
            print("Du gehst durch die Tür im Süden und kommst in den ... ")
            speisesaal()
            break
        elif eingabe == "r":
            rucksackAusgeben()
        else:
            print("Eingabe nicht korrekt. Bitte versuche es erneut.")
def speisesaal():
    print("******************")
    print("*** Speisesaal ***")
    print("******************")
    while(True):
        eingabe = input("Was möchtest du tun? u) Raum untersuchen n) Tür im Norden nutzen r) Rucksack öffnen ... ")
        if eingabe == "u":
            if not rucksack["schluessel"]:
                print("Du entdeckst einen goldenen Schlüssel auf der langen gedeckten Tafel.")
                print("""
         000000
        00  F  00
        00  I  00
         000B000
         00
         00
         00
         00000
         0000
         0000000
       """)      
                print("Du versuchst den Schlüssel zu greifen. Sofort beginnt deine Hand stark an zu brennen. Du ziehst die Hand erschrocken zurück. Der Schlüssel scheint mit einer magischen Barriere geschützt zu sein.")      
                print("Du bemerkst, dass einige Ziegelsteine in der Mauer des Speisesaals eine andere Farbe aufweisen. Du versuchst ein Muster zu erkennen ...")
                zufallszahl = random.randint(6,15)
                fibPrint(zufallszahl)
                fibGesucht = fibCalc(zufallszahl+1)
                ziegelNummer = int(input("Welchen Ziegel in der Reihe möchtest du untersuchen?"))
                if fibGesucht==ziegelNummer:
                    print("Der Zeigel bewegt sich. Die magische Barriere um den Schüssel löst sich auf. Du nimmst den Schlüssel auf der Tafel.")
                    rucksack["schluessel"]=True 
            else:
                print("Du errinerst dich ... hier hast du den Schlüssel gefunden.")
        elif eingabe == "n":
            print("Du gehst durch die Tür im Norden und kommst in die ... ")
            eingangshalle()
            break
        elif eingabe == "r":
            rucksackAusgeben()
        else:
            print("Eingabe nicht korrekt. Bitte versuche es erneut.")

def fibPrint(n:int):
    a=0
    b=1
    while b<n:
        print(b)
        temp = a
        a = b
        b = temp + b

def fibCalc(n:int)->int:
    a=0
    b=1
    while b<n:
        temp = a
        a = b
        b = temp + b
    return b

def rucksackAusgeben():
    print("------- Rucksackinhalt --------")
    if rucksack["schluessel"]:
        print("Schlüssel")
    if rucksack["schwert"]:
        print("Schwert")

def rittersaal():
    print("******************")
    print("*** Rittersaal ***")
    print("******************")
    while(True):
        eingabe = input("Was möchtest du tun? u) Raum untersuchen  s) Tür im Süden nutzen  t) Treppe in das Untergeschoss benutzen r) Rucksack öffnen... ")
        if eingabe == "u":
            if rucksack["schwert"]:
                print("Du siehst die bereits geöffnete und jetzt leere Truhe!")
            else:
                print("Du findest eine True und versuchst sie zu öffnen. Die Truhe ist mit 100 Juwelen bestückt. Es sieht so aus, als ob man die Juwelen bewegen könnte ...")
                print("""
         __________
        /\____;;___\\
       | /         /
       `. ())oo() .
        |\\(%()*^^()^\\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|


""")
                zufallszahl = random.randint(1,20)
                probierCounter = 0
                while(True):
                    zahleneingabe = input("Welches Juwel möchstest du als nächstes bewegen?")
                    if zahleneingabe.isnumeric():
                        zahleneingabeZahl = int(zahleneingabe)
                        probierCounter = probierCounter + 1
                        if(probierCounter > 10):
                            print("Die Kiste gibt einen Elektroschock ab. Du hast zu viele Versuche benötigt. Probiere es späer nochmals!")
                            break
                        if zahleneingabeZahl == zufallszahl:
                            print("Du hast das korrekte Juwel gewählt. Die Truhe öffnet sich und du findest ein Schwert in der Truhe, das du mitnimmst!")
                            rucksack["schwert"] = True
                            break
                        elif zahleneingabeZahl < zufallszahl:
                            print("Du hast die Zahl " + zahleneingabe + " gewählt! Die Truhe öffnet sich nicht, du bemerkst jedoch ein Glitzern auf der rechten Seite der True ...")
                        elif zahleneingabeZahl > zufallszahl:
                            print("Du hast die Zahl " + zahleneingabe + " gewählt! Die Truhe öffnet sich nicht, du bemerkst jedoch ein Glitzern auf der linken Seite der True ...")
                    else:
                        print("Bitte gib eine Zahl ein!")     
        elif eingabe == "t":
            print("Du gehst durch die Treppe in das Untergeschoss ...")
            kerker()
            break
        elif eingabe == "s":
            print("Du gehst durch die Tür im Süden und kommst in die ... ")
            eingangshalle()
            break
        elif eingabe == "r":
            rucksackAusgeben()
        else:
            print("Eingabe nicht korrekt. Bitte versuche es erneut.")
def kerker():
    print("**************")
    print("*** Kerker ***")
    print("**************")
    print(""" Du kommst in den Kerker des Schlosses und stehst vor einem großen Drachen ...

                      ,-,-      
                     / / |      
   ,-'             _/ / /       
  (-_          _,-' `Z_/        
   "#:      ,-'_,-.    \\  _     
    #'    _(_-'_()\     \\" |    
  ,--_,--'                 |    
 / ""                      L-'\ 
 \,--^---v--v-._        /   \ | 
   \_________________,-'      | 
                    \\           
                     \\          
                  \\     
""")
    eingabe = input("Was möchtest du tun? a) Drache angreifen  w) Tür im Westen benutzen r) Rucksack öffnen... ")
    if eingabe == "a":
        print("Du greifst den Drachen an!")
        if rucksack["schwert"]:
            print("Du bekämpfst den Drachen mit dem Schwert und kannst ihn besiegen. Hinter dem Drachen findest du einen Schatz, du wirst reich und setzt dich zur Ruhe!")     
            print("******************")
            print("Spiel gewonnen")
            print("******************")
            exit()
        else:
            print("Du bekämpfst den Drachen mit deinen bloßen Händen und kannst ihn nicht besiegen. Du tritts daher den Rückzug an und gehst zurück durch den Raum im Westen!")
            rittersaal()
    elif eingabe == "w":
        print("Du gehst durch die Tür im Westen und kommst in den ...")
        rittersaal()
    elif eingabe == "r":
            rucksackAusgeben()
    else:
        print("Eingabe nicht korrekt. Bitte versuche es erneut.")
eingangshalle()