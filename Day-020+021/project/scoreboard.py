from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )
