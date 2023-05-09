"""
Wenn der Import so gemacht wird "from turtle import *" dann werden alle Members aus dem Namespace geladen und direkt ohne Dot-Notation verfügbar. Das "verschmutzt" allerdings den Namespace.

Wenn das Turtle-Modul so importiert wird "import turtle" dann wird das Turtle-Modul im Namespace verfügbar und man kann
mit turtle.xxx auf die Members im Modul zugreifen. Die Members des Namespace sind aber ohne Dot-Notation nicht verfügbar.
"""

import turtle
turtle.pensize(5)
seitenlaenge = int(input('Seitenlänge?'))
i=0
while i < 4:
    turtle.forward(seitenlaenge)
    turtle.right(90)
    i = i + 1 