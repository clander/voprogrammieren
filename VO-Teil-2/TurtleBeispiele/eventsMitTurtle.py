# https://openbookproject.net/thinkcs/python/english3e/events.html

import turtle, random

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
schildi = turtle.Turtle()

def forward():
    schildi.forward(30)
    
def left():
    schildi.left(45)
    
def right():
    schildi.right(45)
    
def pen():
    if schildi.isdown():
        schildi.penup()
    else:
        schildi.pendown()    
def exit():
    wn.bye()
    

wn.onkeypress(forward, "Up")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(pen, "p")
wn.onkeypress(exit, "q")

wn.listen()
