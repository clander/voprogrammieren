import turtle
turtle.goto(0, 0)
schritteAnzahl = 13
nMinus2 = 0
nMinus1 = 1
while schritteAnzahl > 0:
    schritteAnzahl = schritteAnzahl - 1
    n = nMinus2 + nMinus1
    i = 0
    while i < 4:
        turtle.forward(n)
        turtle.right(90)
        i = i + 1
    nMinus2 = nMinus1
    nMinus1 = n