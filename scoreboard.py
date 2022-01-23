from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.file = open("highest_score.txt")
        self.high_score = int(self.file.read())
        print(self.high_score)
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"score: {self.score} high score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
# 2. replacing game_over() with reset()
    """def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f"game over! Your score is: {self.score}", align=ALIGNMENT, font=FONT)"""

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.file.close()
            with open("highest_score.txt", mode="w") as self.file:
                self.file.write(str(self.high_score))
            self.score = 0
            self.update_score()
