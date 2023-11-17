# https://openbookproject.net/thinkcs/python/english3e/events.html

import turtle, random

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")

def onForward():
    turtle.forward(30)
    
def onLeft():
    turtle.left(45)
    
def onRight():
    turtle.right(45)
    
def onPen():
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()    
def onExit():
    wn.bye()
    

wn.onkeypress(onForward, "Up")
wn.onkeypress(onLeft, "Left")
wn.onkeypress(onRight, "Right")
wn.onkeypress(onPen, "p")
wn.onkeypress(onExit, "q")

wn.listen()
