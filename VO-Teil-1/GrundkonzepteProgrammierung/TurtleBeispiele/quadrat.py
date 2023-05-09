import turtle
turtle.pensize(5)
seitenlaenge = int(input('Seitenlänge?'))
i=0
while i < 4:
    turtle.forward(seitenlaenge)
    turtle.right(90)
    i = i + 1 