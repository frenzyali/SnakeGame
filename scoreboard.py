from turtle import Turtle
data = open("data.txt")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(data.read())
        data.close()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align='center', font=('Arial', 20, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open("data.txt", "w")
            file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


