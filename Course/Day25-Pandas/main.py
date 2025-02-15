import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data["state"] == answer_state]
        x_coordinate = state_data["x"].values[0]
        y_coordinate = state_data["y"].values[0]
        new_state = turtle.Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(x_coordinate, y_coordinate)
        new_state.write(answer_state, font=("Arial", 10, "bold"))
