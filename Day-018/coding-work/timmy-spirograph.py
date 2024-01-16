from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
timmy.shape("turtle")
timmy.color("dark green")

screen = Screen()
screen.colormode(255)


def random_color():
    rgb_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return rgb_color


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.circle(150)
        timmy.setheading(timmy.heading() + gap_size)


timmy.pensize(1)
timmy.speed("fastest")

draw_spirograph(2)

screen.exitonclick()
