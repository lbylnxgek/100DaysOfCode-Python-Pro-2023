from turtle import Turtle, Screen
from random import randint, choice

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


def random_direction():
    directions = [0, 90, 180, 270]
    direction = choice(directions)
    return direction


timmy.pensize(7)
timmy.speed("fastest")
for _ in range(300):
    timmy.pencolor(random_color())
    heading = random_direction()
    timmy.setheading(random_direction())
    timmy.forward(20)


screen.exitonclick()
