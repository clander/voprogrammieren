import turtle
ecken = int(input("Wieviele Ecken?"))
seitenlaenge = int(input("Seitenlänge?"))
i = 0
while i < ecken:
    turtle.forward(seitenlaenge)
    turtle.right(360/ecken)
    i = i +1
