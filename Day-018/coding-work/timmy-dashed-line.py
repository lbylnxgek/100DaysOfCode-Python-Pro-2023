from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("dark green")
screen = Screen()

# Draw a dashed line
for _ in range(0, 15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.exitonclick()
