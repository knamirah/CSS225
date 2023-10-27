# Namirah
# 10/20

# Write a program to draw some kind of picture. Be creative and experiment with the turtle methods provided in Summary of Turtle Methods.

import math

radius = int(input("What is the radius of the flower?"))
petals = int(input("How many petals do you want?"))


def draw_arc(b, r):
    c = 2 * math.pi * r
    ca = c / (360 / 60)
    n = int((ca / 3) + 1)
    l = ca / n
    for _ in range(n):
        b.fd(1)
        b.lt(360 / (n * 6))


def draw_petal(b, r):
    draw_arc(b, r)
    b.lt(180 - 60)
    draw_arc(b, r)


import turtle

bob = turtle.Turtle()

for i in range(petals):
    draw_petal(bob, radius)
    bob.lt(360 / petals)

turtle.mainloop()
