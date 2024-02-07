from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        with open("high_score.txt") as score_data:
            self.high_score = int(score_data.read())
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as score_data:
                score_data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
