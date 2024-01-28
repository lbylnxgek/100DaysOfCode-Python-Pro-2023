from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")

# Create turtle to draw dashed centerline
screen.tracer(0)
center_line = Turtle()
center_line.shape("arrow")
center_line.color("white")
center_line.penup()
center_line.goto(0, 300)
center_line.setheading(270)
center_line.width(2)

# Draw a dashed line
for _ in range(0, 29):
    center_line.forward(10)
    center_line.penup()
    center_line.forward(10)
    center_line.pendown()

center_line.hideturtle()
screen.update()


screen.exitonclick()
