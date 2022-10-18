from tkinter import scrolledtext
from tracemalloc import start
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)


game = True
no_collision = True
screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkeypress(key="a", fun=snake.left)
screen.onkeypress(key="d", fun=snake.right)
screen.onkeypress(key="w", fun=snake.up)
screen.onkeypress(key="s", fun=snake.down)

while game and no_collision:
    screen.update()  # will update screen for the entire image, in for loop we see one by one
    time.sleep(0.1)
    snake.move_fd()

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend_snake()

    game = snake.lose()
    no_collision = snake.detect_collision()

scoreboard.game_over()
screen.exitonclick()
