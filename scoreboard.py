from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=("Courier", 25, "normal"))