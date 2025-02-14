from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.speed("fastest")
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)