import turtle
seitenlaenge = 10
while seitenlaenge < 100:
    seiten = 2
    while seiten > 0:
        turtle.forward(seitenlaenge)
        turtle.right(90)
        seiten = seiten - 1
    seitenlaenge = seitenlaenge + 5