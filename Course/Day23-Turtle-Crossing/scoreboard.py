from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 0
        self.goto(-210, 250)
        self.display_scoreboard()

    def display_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.display_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
