import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "Day25-/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


states = pandas.read_csv("Day25-/us-states-game-start/50_states.csv")

turtle.onscreenclick(get_mouse_click_coor)
original_states = states
t = turtle.Turtle()
t.pu()
t.hideturtle()

good_guesses = []
game = True
score = 0
turtle.pu()
print(len(states))
while game:
    state = ""
    answer_state = screen.textinput(
        title=f"{score}/{len(original_states)}Guess the State", prompt="Another State ?").title()

    if answer_state in original_states["state"].values:
        score += 1
        state = states[states.state != answer_state]  # DataFrame
        states = states.loc[states['state'] != answer_state]
        print(states)
        # get x and y
        state_list = state.values.tolist()[0]
        # print(state_list)
        pos_x = int(state_list[1])
        pos_y = int(state_list[2])
        t.goto((pos_x, pos_y))
        t.write(answer_state)
        good_guesses = answer_state


turtle.mainloop()

# screen.exitonclick()
