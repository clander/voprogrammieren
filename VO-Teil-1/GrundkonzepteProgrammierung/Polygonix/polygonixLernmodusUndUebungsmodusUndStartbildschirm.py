import turtle, random, sys

def zahlenEingabe(ausgabetext: str, minimum: int, maximum: int) -> int:
    eingabeKorrekt = False
    while not eingabeKorrekt:
        print(ausgabetext + ' Bitte Zahlen zwischen ' + str(minimum) + ' und ' + str(maximum) + ' eingeben!')
        try:
            eingabe = int(input())
            if eingabe >= minimum and eingabe <= maximum:
                eingabeKorrekt = True
        except Exception as e:
            pass # Hier könnte man auf die Exception reagieren
            
    return eingabe

def booleanEingabe(ausgabetext: str) -> bool:
    eingabe = ''
    while eingabe != 'j' and eingabe != 'n':
        print(ausgabetext + ' [j] für Ja, [n] für Nein')
        eingabe = input()
    if eingabe == 'j':
        return True
    elif eingabe == 'n':
        return False
    else:
        return False

def farbenEingabe(farben:list[str]) -> str:
    for i in range(1,len(farben)):
        print(str(i) +') ' + farben[i])
    eingabe = ''
    while eingabe not in farben:
        eingabe = input('Bitte Farbe eingeben:')
    return eingabe

def zufallsfarbe(farben:list[str])->str:
    zufallFarbe = farben[random.randint(0, len(farben)-1)]
    return zufallFarbe
                    
def polygonZeichnenMitZufallsfarbe(anzahlEcken: int, seitenlaenge: int, dicke: int, farbenliste:list[str]):
    turtle.pensize(dicke)
    i = 0
    while i < anzahlEcken:
        turtle.pencolor(zufallsfarbe(farbenliste))
        turtle.forward(seitenlaenge)
        turtle.right(360 / anzahlEcken)
        i = i + 1

def polygonZeichnenMitFarbe(anzahlEcken: int, seitenlaenge: int, dicke: int, farbe: str):
    turtle.pensize(dicke)
    for i in range(0,anzahlEcken):##Alternative zu While, insb. wenn man i als Zähler braucht
        turtle.pencolor(farbe)
        turtle.forward(seitenlaenge)
        turtle.right(360 / anzahlEcken)

# Moduswahl
def moduswahl()->str:
    eingabe = ''
    while eingabe != 'l' and eingabe != 'u' and eingabe != 'x':
        print("Wähle L für Lernmodus, U für Übungsmodus und X um das Programm zu verlassen!")
        eingabe = input()
        eingabe = eingabe.lower()
    return eingabe.lower();

# Startbildschirm zeichnen
def zeichneStartbildschirm():
    meineFarben = farbenArray = ['blue', 'red', 'green', 'yellow', 'black', 'orange','violet','pink','brown']
    turtle.speed(0) #fastest speed
    for i in range(random.randint(7,15)): 
        polygonZeichnenMitZufallsfarbe(random.randint(3,7),random.randint(40,70),random.randint(1,3),meineFarben)
        turtle.forward(50)
        turtle.right(34)
    turtle.speed(3) # normal speed

# Turtle und Bildschirm zurücksetzen
def reset():
    turtle.clear()
    turtle.penup()
    turtle.setx(0)
    turtle.sety(0)
    turtle.speed(3)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")


zeichneStartbildschirm()
modus = moduswahl()
while modus != 'x':
    if modus == 'l':
        reset()
        print("**** LERNMODUS ***")
        #Eingaben des Benutzers:
        zufallsfarbenWahl = booleanEingabe('Zufallsfarben?')
        ecken = zahlenEingabe('Wieviele Ecken?',3 , 10)
        laenge = zahlenEingabe('Seitenlänge? ',40,100)
        strichdicke = zahlenEingabe('Strich-Dicke?',1,4)

        #Polygon auf Basis der Eingaben Zeichnen:
        farbenArray = ['blue', 'red', 'green', 'yellow', 'black', 'orange','violet','pink','brown']

        if zufallsfarbenWahl:
            polygonZeichnenMitZufallsfarbe(ecken,laenge,strichdicke,farbenArray)
        else:
            farbwahl = farbenEingabe(farbenArray)
            polygonZeichnenMitFarbe(ecken,laenge,strichdicke,farbwahl)
        modus = moduswahl()
    elif modus == 'u':
        reset()
        print("**** Übungsmodus ***")
        zufall = random.randint(3,10)
        polygonZeichnenMitFarbe(zufall,80,4,"black")
        antwort = zahlenEingabe("Um welche Art von geometrischer Figur handelt es sich? 3) Dreieck 4) Viereck 5) Fünfeck usw.",3,10)
        if antwort == zufall:
            print("Richtig!")
        else:
            print("Leider noch nicht richtig. Versuche es nochmal und zähle genau!")
        modus = moduswahl()

print("Auf wiedersehen")
sys.exit()
