from turtle import Screen, Turtle, color
import colorgram
from random import randrange, choice

tim = Turtle()
screen = Screen()

tim.speed(0)

colors = colorgram.extract("Day18_turtle\hirsh.png", 20)  # extracting colors


def draw_hirsh_line(turtle, screen, colors, size, n_columns):
    screen.colormode(255)
    for row in range(n_columns):
        color = choice(colors)  # choosing color
        turtle.pencolor(color.rgb)
        turtle.dot(20)  # draws a dot
        turtle.forward(size/n_columns)  # moves a certain distance


def complete_hirsh(turtle, screen, n_rows, n_columns, colors):
    FULL_SIZE = 400
    turtle.pu()  # no line
    current_y = -FULL_SIZE/2
    turtle.goto(-FULL_SIZE/2, current_y)  # initial position

    for dot in range(n_rows):
        draw_hirsh_line(turtle, screen, colors, FULL_SIZE, n_columns)
        current_y += FULL_SIZE/n_rows  # increment position for next row
        turtle.goto(-FULL_SIZE/2, current_y)  # move to next row
    turtle.ht()  # hides cursor at the end


n_rows = 10
n_columns = 10

complete_hirsh(tim, screen, n_rows, n_columns, colors)

screen.exitonclick()
