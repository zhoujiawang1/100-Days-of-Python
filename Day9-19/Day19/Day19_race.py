from turtle import Turtle, Screen
from random import choice, randint
import turtle


screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Make Your Bet",
                       prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "purple", "yellow", "green", "blue", "blue"]
speed = ["fastest", "fast", "normal", "slow", "slowest"]

SPACING = 200/6
pos_y = 100

tim1 = Turtle(shape="turtle")
tim2 = Turtle(shape="turtle")
tim3 = Turtle(shape="turtle")
tim4 = Turtle(shape="turtle")
tim5 = Turtle(shape="turtle")
tim6 = Turtle(shape="turtle")

turtle_tab = [
    tim1, tim2, tim3, tim4, tim5, tim6
]

for num in range(len(turtle_tab)):
    turtle_tab[num].pu()
    turtle_tab[num].goto(x=-200, y=pos_y)
    turtle_tab[num].color(colors[num])
    pos_y -= SPACING

game = True
winner = ""
while game:
    for num in range(len(turtle_tab)):
        turtle_tab[num].speed(choice(speed))
        turtle_tab[num].forward(randint(10, 50))
        if turtle_tab[num].pos()[0] >= 250:
            game = False
            winner = colors[num]

if bet == winner:
    print("You win!")
else:
    print(f"You lose. The winner is {winner}")
screen.exitonclick()
