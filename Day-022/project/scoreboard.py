from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 230)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(50, 230)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

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

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
