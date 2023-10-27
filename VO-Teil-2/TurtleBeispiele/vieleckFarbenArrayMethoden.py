import turtle, random

def zahlenEingabe(ausgabetext: str, minimum: int, maximum: int) -> int:
    eingabeKorrekt = False
    while not eingabeKorrekt:
        print('Bitte Zahlen dzwischen ' + str(minimum) + ' und ' + str(maximum) + ' eingeben!')
        try:
            eingabe = int(input(ausgabetext))
            print(type(eingabe))
            if eingabe >= minimum and eingabe <= maximum:
                eingabeKorrekt = True
        except Exception as e:
            pass # Hier könnte man auf die Exception reagieren
            
    return eingabe

def booleanEingabe(ausgabetext: str) -> bool:
    eingabe = ''
    while eingabe != 'j' and eingabe != 'n':
        print('j für Ja, n für Nein')
        eingabe = input(ausgabetext)
        print('Eingabe: ' + eingabe)
    if eingabe == 'j':
        return True
    elif eingabe == 'n':
        return False
    else:
        return False

def zufallsfarbe(farben:list[str])->str:
    zufallFarbe = farben[random.randint(0, len(farben)-1)]
    return zufallFarbe
                    
def polygonZeichnenMitZufallsfarbe(anzahlEcken: int, seitenlaenge: int,dicke: int, farbenliste:list[str]):
    turtle.pensize(dicke)
    i = 0
    while i < anzahlEcken:
        turtle.pencolor(zufallsfarbe(farbenliste))
        turtle.forward(seitenlaenge)
        turtle.right(360 / ecken)
        i = i + 1

def polygonZeichnenMitFarbe(anzahlEcken: int, seitenlaenge: int, dicke: int, farbe: str):
    turtle.pensize(dicke)
    for i in range(0,anzahlEcken):##Alternative zu While, insb. wenn man i als Zähler braucht
        turtle.pencolor(farbe)
        turtle.forward(seitenlaenge)
        turtle.right(360 / ecken)

def farbenEingabe(farben:list[str]) -> str:
    for i in range(1,len(farben)):
        print(str(i) +') ' + farben[i])
    eingabe = ''
    while eingabe not in farben:
        eingabe = input('Bitte Farbe eingeben:')
    return eingabe
    
#Eingaben des Benutzers:
zufallsfarbenWahl = booleanEingabe('Zufallsfarben?')
ecken = zahlenEingabe('Wieviele Ecken?',3 , 50)
laenge = zahlenEingabe('Seitenlänge? ',10,100)
strichdicke = zahlenEingabe('Strich-Dicke?',1,10)

#Polygon auf Basis der Eingaben Zeichnen:
farbenArray = ['blue', 'red', 'green', 'yellow', 'black', 'orange','violet','pink','brown']

if zufallsfarbenWahl:
    polygonZeichnenMitZufallsfarbe(ecken,laenge,strichdicke,farbenArray)
else:
    farbwahl = farbenEingabe(farbenArray)
    polygonZeichnenMitFarbe(ecken,laenge,strichdicke,farbwahl)
