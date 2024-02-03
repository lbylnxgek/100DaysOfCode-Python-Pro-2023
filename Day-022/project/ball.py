from turtle import Turtle
import random

DEBUG = False


class Ball(Turtle):
    def __init__(self) -> None:
        """Create ball object"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        if DEBUG:
            print(f"DEBUG: x:{self.xcor()}, {self.x_move}")
            print(f"DEBUG: y:{self.ycor()}, {self.y_move}")
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collide_with_wall(self):
        return self.ycor() > 280 or self.ycor() < -280

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
