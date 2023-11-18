import turtle
eingabe = input("Wieviele Ecken soll die Figur haben?")
eingabe_zahl = int(eingabe)
zaehler = 0
turtle.pensize(4)
schalter = True;
while zaehler < eingabe_zahl:
    if schalter:
        turtle.pencolor('blue')
        schalter = not schalter
    else:
        turtle.pencolor('black')
        schalter = not schalter
    turtle.forward(100)
    turtle.right(360/eingabe_zahl)
    zaehler = zaehler + 1