###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations

import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

pen.penup()
pen.goto(-150, 100)
pen.pendown()
figures.draw_square(pen, 60)

pen.penup()
pen.goto(50, 100)
pen.pendown()
figures.draw_square(pen, 40)

pen.penup()
pen.goto(-150, -20)
pen.pendown()
figures.draw_triangle(pen, 80)

pen.penup()
pen.goto(50, -20)
pen.pendown()
figures.draw_triangle(pen, 50)

pen.penup()
pen.goto(-150, -150)
pen.pendown()
figures.draw_rectangle(pen, 100, 50)

pen.penup()
pen.goto(50, -150)
pen.pendown()
figures.draw_rectangle(pen, 60, 30)

pen.hideturtle()
window.mainloop()
