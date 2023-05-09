import turtle
ecken = int(input("Wieviele Ecken?"))
seitenlaenge = int(input("Seitenlänge?"))
stiftdicke = int(input("Wie dick sollen die Linien sein?"))
turtle.pensize(stiftdicke)
i = 0
while i < ecken:
    if i % 2 == 0:
        farbe = "red"
    else:
        farbe = "black"
    turtle.pencolor(farbe)
    turtle.forward(seitenlaenge)
    turtle.right(360/ecken)
    i = i +1