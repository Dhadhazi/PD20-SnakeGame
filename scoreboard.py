from turtle import Turtle

class Scroreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0;
        self.pencolor("white")
        self.write_score()


    def write_score(self):
        self.goto(0, 260)
        self.write(f"Score : {self.score}", True, align="center", font=("Arial", 25))

    def increse_score(self):
        self.score += 1;
        self.clear()
        self.write_score()
