from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.all_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.all_segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            self.all_segments[seg_num].goto(self.all_segments[seg_num - 1].pos())
        self.all_segments[0].forward(MOVE_DISTANCE)
