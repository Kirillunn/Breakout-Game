from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(arg=f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

