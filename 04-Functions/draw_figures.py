###
# Draw a square using function from figures module
#
import turtle
import figures   # nasz moduł z funkcjami

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw square
figures.draw_square(pen, 100)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
