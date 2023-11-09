#Namirah
#11/8/2023

#Use the following chunk of code as a base to produce the image shown below.

import turtle

def drawSquare(t,sz):
    """"Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
len = 50
for i in range(5):
    drawSquare(alex, len)
    alex.right(135)
    alex.penup()
    alex.forward(7.5)
    alex.left(135)
    alex.pendown()
    len += 10


wn.exitonclick()