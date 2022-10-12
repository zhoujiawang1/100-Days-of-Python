from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fd():
    tim.forward(10)


def move_bd():
    tim.backward(10)


def rotate_cw():
    tim.right(5)


def rotate_ccw():
    tim.left(5)


def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()

screen.onkeypress(key="space", fun=clear)
screen.onkeypress(key="w", fun=move_fd)
screen.onkeypress(key="s", fun=move_bd)
screen.onkeypress(key="d", fun=rotate_cw)
screen.onkeypress(key="a", fun=rotate_ccw)

screen.exitonclick()
