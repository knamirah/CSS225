#Namirah
#10/20

#Write a program that asks the user for the number of sides, the length of the side, the color of the line, and the fill color of a regular polygon. The program should draw the polygon and then fill it in.

import turtle
wn = turtle.Screen()
Khan = turtle.Turtle()

color = input("pick a color")
Khan.color(color)

number_sides = int(input("how many sides"))
fill_color = input("what is the fill color")
Khan.fillcolor(fill_color)
Khan.begin_fill()
side = int(input("enter the length"))


for i in range(number_sides):      # repeat four times
    Khan.forward(side)
    Khan.left(360/number_sides)
Khan.end_fill()
wn.exitonclick()
