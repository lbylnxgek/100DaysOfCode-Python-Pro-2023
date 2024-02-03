from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self) -> None:
        """Create ball object"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def collide_with_wall(self):
        return self.ycor() > 295 or self.ycor() < -295
