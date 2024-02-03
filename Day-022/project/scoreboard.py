from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.r_score = 0
        self.l_score = 0

    def draw_centerline(self):
        """Create dashed centerline"""
        line = Turtle()
        line.shape("arrow")
        line.color("white")
        line.penup()
        line.goto(0, 300)
        line.setheading(270)
        line.width(2)

        # Draw a dashed line
        for _ in range(0, 29):
            line.forward(10)
            line.penup()
            line.forward(10)
            line.pendown()

        line.hideturtle()
