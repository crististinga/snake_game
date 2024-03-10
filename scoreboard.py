from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.pendown()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.counter} High score: {self.highscore}")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER")
