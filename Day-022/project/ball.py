from turtle import Turtle
import random

SERVE_DIRECTIONS = (
    0,
    15,
    30,
    45,
    135,
    150,
    165,
    180,
    195,
    210,
    225,
    315,
    330,
    345,
)


class Ball(Turtle):
    def __init__(self) -> None:
        """Create ball object"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.forward(5)

    def serve(self):
        self.setheading(random.choice(SERVE_DIRECTIONS))
