from turtle import Turtle, Screen
from random import randrange
import turtle

tim = Turtle()
tim.shape("turtle")
screen = Screen()


def dashed_line(turtle, length, n):
    '''takes the turtle obj and for a length will draw n lines'''
    for i in range(n-1):
        turtle.fd(length/(n+n-1))  # travel an n distance
        turtle.pu()  # no drawing

        turtle.fd(length/(n+n-1))  # travel an n distance
        turtle.pd()  # no drawing


def draw_shape(turtle, screen, num_sides):
    ONE_TURN = 360
    angle = ONE_TURN/num_sides
    screen.colormode(255)
    turtle.pencolor((randrange(0, 255)), (
        randrange(0, 255)), (randrange(0, 255)))
    for turn in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


def random_walk(turtle, screen, distance, num_lines):
    screen.colormode(255)
    turtle.pensize(15)
    turtle.speed(0)
    for step in range(num_lines):
        turtle.pencolor(((randrange(0, 255)), (
            randrange(0, 255)), (randrange(0, 255))))
        turtle.right(randrange(0, 4)*90)
        turtle.fd(distance)


def draw_spirograph(turtle, screen, n_circle):
    screen.colormode(255)
    turtle.speed(0)
    ONE_TURN = 360
    angle = ONE_TURN/n_circle
    for step in range(n_circle):
        turtle.pencolor(((randrange(0, 255)), (
            randrange(0, 255)), (randrange(0, 255))))
        turtle.circle(100)
        turtle.right(angle)


# for i in range(4): #draws a square
#     tim.dot()
#     tim.forward(100)
#     tim.right(90)
# dashed_line(tim, 200, 10)

# for i in range(3, 12):
#     draw_shape(tim, screen, i)
# random_walk(tim, screen, 100, 200)
draw_spirograph(tim, screen, 100)


screen.exitonclick()  # wont dissapear but it has to be at the end
