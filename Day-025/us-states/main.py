import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create turtle to write state names
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

    # Check for exit condition
    if answer_state == "Exit":
        # Create list of states to learn
        states_to_learn = []
        for state in states_list:
            if state not in correct_guesses:
                states_to_learn.append(state)

        # Create dictionary
        data_dict = {"State": states_to_learn}

        # Create dataframe and write to CSV
        df = pandas.DataFrame(data_dict)
        df.to_csv("states_to_learn.csv")
        break

    # Check for correct guess
    if answer_state in states_list and answer_state not in correct_guesses:
        state_data = data[data.state == answer_state]
        state_turtle.goto(int(state_data.x), int(state_data.y))
        state_turtle.write(state_data.state.item())
        correct_guesses.append(state_data.state.item())
