import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.up()
        self.hideturtle()
        self.goto(0, 260)
        self.display()

    def display(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))