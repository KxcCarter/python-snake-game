from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.write("Score: 0", False, align="center", font=("Arial", 24, "normal"))

    score = 0

    def add_point(self):
        self.score += 1
        self.clear()
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

