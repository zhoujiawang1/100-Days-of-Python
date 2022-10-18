from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.write(f"Score {self.score}", True,
                   align='center', font=("Arial", 21, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score {self.score}", True,
                   align='center', font=("Arial", 21, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over", True,
                   align='center', font=("Arial", 21, "normal"))
