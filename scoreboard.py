from turtle import Turtle
ALIGN = 'center'
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGN, font=FONT)