from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("dark green")
screen = Screen()

# Draw a square
for _ in range(0, 4):
    timmy.forward(100)
    timmy.right(90)

screen.exitonclick()
