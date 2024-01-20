# This section of code is used to generate color_list from an image
# and is not needed once that has been done
# import colorgram

# colors = colorgram.extract("image.jpg", 50)
# rgb_list = []


# for color in colors:
#     rgb = color.rgb
#     rgb_tuple = (rgb.r, rgb.g, rgb.b)
#     rgb_list.append(rgb_tuple)


# print(rgb_list)

# Note: RGB tuples with high values should be checked as they may be part of the
# original image background and too light for dots
color_list = [
    (198, 166, 109),
    (141, 77, 54),
    (73, 98, 123),
    (158, 148, 54),
    (213, 203, 144),
    (120, 39, 29),
    (137, 160, 179),
    (70, 108, 74),
    (144, 176, 139),
    (195, 91, 70),
    (69, 52, 46),
    (96, 81, 89),
    (60, 52, 56),
    (224, 177, 163),
    (102, 141, 131),
    (97, 130, 164),
    (156, 141, 159),
    (49, 60, 83),
    (73, 67, 50),
    (111, 38, 42),
    (47, 56, 72),
    (108, 136, 140),
    (182, 199, 183),
    (182, 190, 205),
    (168, 101, 106),
    (51, 76, 61),
    (213, 181, 184),
    (180, 195, 199),
    (38, 68, 66),
    (43, 81, 82),
]

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.title("Timmy draws Hirst")
screen.colormode(255)
screen.setworldcoordinates(-5, -5, 97, 97)

for y in range(0, 100, 10):
    for x in range(0, 100, 10):
        # print(f"coords: {x}, {y}")
        timmy.dot(20, random.choice(color_list))
        timmy.teleport(x, y)

timmy.dot(20, random.choice(color_list))
timmy.hideturtle()

screen.exitonclick()
