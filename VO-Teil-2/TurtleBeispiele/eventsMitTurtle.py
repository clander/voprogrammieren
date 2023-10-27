# https://openbookproject.net/thinkcs/python/english3e/events.html

import turtle, random

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def forward():
    tess.forward(30)
    
def left():
    tess.left(45)
    
def right():
    tess.right(45)
    
def pen():
    if tess.isdown():
        tess.penup()
    else:
        tess.pendown()    
def exit():
    wn.bye()
    

wn.onkeypress(forward, "Up")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(pen, "p")
wn.onkeypress(exit, "q")

wn.listen()
