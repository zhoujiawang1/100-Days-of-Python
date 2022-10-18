from turtle import Turtle, Screen
from food import Food
STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVING_INCREMENT = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        sq = Turtle("square")
        sq.pu()
        sq.color("white")
        sq.goto(position)
        self.squares.append(sq)

    def extend_snake(self):
        self.add_segment(self.squares[-1].position())

    def move_fd(self):
        for sq in range(len(self.squares)-1, 0, -1):
            # squares[sq].fd(MOVING_INCREMENT)
            new_x = self.squares[sq - 1].xcor()
            new_y = self.squares[sq - 1].ycor()
            self.squares[sq].goto(new_x, new_y)
        self.squares[0].fd(MOVING_INCREMENT)

    def up(self):
        if self.head.heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.squares[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def detect_collision(self):
        for sq in self.squares:
            if sq == self.head:
                pass
            elif self.head.distance(sq) < 10:
                return False

            return True

    def lose(self):
        if self.head.xcor() <= -280 or self.head.xcor() >= 280 or self.head.ycor() >= 280 or self.head.ycor() <= -280:
            return False
        else:
            return True
