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
        eingabe = input("Was möchtest du tun? u) Raum untersuchen  n) Tür im Norden nutzen  s) Tür im Süden nutzen ... ")
        if eingabe == "u":
            print("Du findest nichts.")
        elif eingabe == "n":
            if rucksack["schluessel"]:
                print("Du verwendest den Schlüssel und gehst durch die Tür im Norden")
                rittersaal()
            else:
                print("Die Tür ist versperrt, du kommst da nicht durch!")
        elif eingabe == "s":
            print("Du gehst durch die Tür im Süden und kommst in den ... ")
            speisesaal()
        else:
            print("Eingabe nicht korrekt. Bitte versuche es erneut.")
  
def speisesaal():
    print("******************")
    print("*** Speisesaal ***")
    print("******************")
    while(True):
        eingabe = input("Was möchtest du tun? u) Raum untersuchen  n) Tür im Norden nutzen ... ")
        if eingabe == "u":
            print("Du siehst dich um und entdeckst hinter einem Brett einen Schlüssel am Boden. Du nimmst den Schlüssel auf!")
            rucksack["schluessel"]=True 
        elif eingabe == "n":
            print("Du gehst durch die Tür im Norden und kommst in die ... ")
            eingangshalle()
        else:
            print("Eingabe nicht korrekt. Bitte versuche es erneut.")

def rittersaal():
    print("******************")
    print("*** Rittersaal ***")
    print("******************")
    while(True):
        eingabe = input("Was möchtest du tun? u) Raum untersuchen  s) Tür im Süden nutzen  t) Treppe in das Untergeschoss benutzen ... ")
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
        elif eingabe == "s":
            print("Du gehst durch die Tür im Süden und kommst in die ... ")
            eingangshalle()
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
    eingabe = input("Was möchtest du tun? a) Drache angreifen  w) Tür im Westen benutzen ... ")
    if eingabe == "a":
        print("Du greifst den Drachen an!")
        if rucksack["schwert"]:
            print("Du bekämpfst den Drachen mit dem Schwert und kannst ihn besiegen. Hinter dem Drachen findest du einen Schatz, du wirst reich und setzt dich zur Ruhe!")     
            gameOver()
        else:
            print("Du bekämpfst den Drachen mit deinen bloßen Händen und kannst ihn nicht besiegen. Du tritts daher den Rückzug an und gehst zurück durch den Raum im Westen!")
            rittersaal()
    elif eingabe == "w":
        print("Du gehst durch die Tür im Westen und kommst in den ...")
        rittersaal()
    else:
        print("Eingabe nicht korrekt. Bitte versuche es erneut.")

def gameOver():
    print("******************")
    print("* Spiel gewonnen *")
    print("******************")
    sys.exit()

eingangshalle()


