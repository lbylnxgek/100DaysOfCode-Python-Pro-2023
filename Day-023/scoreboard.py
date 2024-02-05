from turtle import Turtle

LEVEL_FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=LEVEL_FONT)

    def increase_level(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=GAME_OVER_FONT)
