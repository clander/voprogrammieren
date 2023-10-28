import turtle, random

def zufallsFarbe()->str:
    farben = ['blue', 'red', 'green', 'yellow', 'black']
    return farben[random.randint(0, 4)]

def zahlenEingabe(prompt:str, minimum:int, maximum:int)->int:
    eingabeKorrekt = False
    while not eingabeKorrekt:
        try:
            zahl = int(input(prompt))
            if zahl>=minimum and zahl <= maximum:
                eingabeKorrekt = True
            else:
                print("Zahl muss zwischen " + str(minimum) + " und " + str(maximum) + " liegen!")
        except Exception as e:
            print(e)
            print("Eingabe muss eine Zahl sein!")
    return zahl

ecken = zahlenEingabe('Wieviele Ecken?',3,10)
seitenlaenge = zahlenEingabe('Seitenlänge?',10,100)
i = 0
while i < ecken:
    zufallFarbe = zufallsFarbe()
    turtle.pencolor(zufallFarbe)
    turtle.forward(seitenlaenge)
    turtle.right(360 / ecken)
    i = i + 1