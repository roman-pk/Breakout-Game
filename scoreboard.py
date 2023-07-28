from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('dark grey')
        self.penup()
        self.hideturtle()
        # Score, lives, speed,
        self.score = 0
        self.lives = 3
        self.speed = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 330)
        self.write(f"Score:{self.score} | Lives: {self.lives} | Speed: {self.speed} ", align='center', font=("Courier", 40, "normal"))
        self.goto(-500, 310)
        self.pendown()
        self.pensize(10)
        self.goto(500,310)
        self.penup()

    def increase_score(self, points):
        self.score +=points
        self.update_scoreboard()

    def lower_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def increase_speed(self, bool):
        if bool == True:
            self.speed += 1
            self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=("Courier", 60, "normal"))

    def you_won(self):
        self.goto(0, 0)
        self.write(f"YOU WON", align='center', font=("Courier", 60, "normal"))