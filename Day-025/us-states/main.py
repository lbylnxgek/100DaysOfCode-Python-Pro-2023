import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()

# This code will allow you to plot x & y values for a background image
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(
        title=f"{len(correct_guesses)}/50 states correct",
        prompt="What's another state's name?",
    ).title()
    print(answer_state)

    # Check for correct guess
    if answer_state in states_list and answer_state not in correct_guesses:
        state_data = data[data.state == answer_state]
        state_turtle.goto(int(state_data.x), int(state_data.y))
        state_turtle.write(state_data.state.item())
        correct_guesses.append(state_data.state.item())
        print(correct_guesses)

screen.exitonclick()
