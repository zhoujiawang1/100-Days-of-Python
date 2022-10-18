from operator import index
import turtle
import pandas

# constant
PATH_IMG = "Day25-/us-states-game-start/"
PATH_CSV = "Day25-/us-states-game-start/50_states.csv"


def get_mouse_click_coor(x, y):
    print(x, y)


# set up scren
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coor)

# for writing on screen
t = turtle.Turtle()
t.pu()
t.hideturtle()
turtle.pu()

# opening file
states = pandas.read_csv("50_states.csv")
original_states = states  # in case it changes

missing_states = states

good_guesses = []
game = True
score = 0


while game:
    state = ""
    answer_state = screen.textinput(
        title=f"{score}/{len(original_states)}Guess the State", prompt="Another State ?").title()

    if answer_state == 'Exit':
        game == False
        break
    if answer_state in original_states["state"].values:
        # increases score
        score += 1

        # gets the index
        index_obj = states.index[states["state"] == answer_state]
        index_ans = states.index[states["state"] == answer_state][0]
        # makes a list with the ans state and its coords
        state_list = states.values.tolist()[index_ans]

        # write state name on map
        pos_x = int(state_list[1])
        pos_y = int(state_list[2])
        t.goto((pos_x, pos_y))
        t.write(answer_state)

        # removing row that contains the state
        missing_states = missing_states.loc[missing_states.state != answer_state]

        print(state_list)

        good_guesses = answer_state

missing_states.to_csv("Missing States.csv")
states.to_csv("States.csv")
turtle.mainloop()

# screen.exitonclick()
