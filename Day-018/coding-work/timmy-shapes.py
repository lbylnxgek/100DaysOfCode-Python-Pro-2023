from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("turtle")
timmy.color("dark green")
screen = Screen()
screen.colormode(255)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


def random_color():
    rgb_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return rgb_color


for shape in range(3, 11):
    color = random_color()
    timmy.pencolor(color)
    draw_shape(shape)


screen.exitonclick()
