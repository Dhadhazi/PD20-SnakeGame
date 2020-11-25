from turtle import Turtle

class Scroreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0;
        self.high_score = self.get_high_score();
        self.pencolor("white")
        self.write_score()

    @staticmethod
    def get_high_score():
        with open("data.txt") as file:
            score = file.read()
            if score == '':
                score = 0
            return int(score)

    @staticmethod
    def set_high_score(score):
        with open("data.txt", mode="w") as file:
            file.write(str(score))

    def write_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align="center", font=("Arial", 25))

    def reset(self):
        if self.score > self.high_score:
            self.set_high_score(self.score)
            self.high_score = self.score
        self.score = 0
        self.write_score()

    def increse_score(self):
        self.score += 1;
        self.write_score()
