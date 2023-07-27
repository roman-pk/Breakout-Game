from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("Blue")
        self.shapesize(1, 14)
        self.penup()
        self.goto(0, -360)
        self.move_distance = 50

    def go_left(self):
        # limit the paddle movement within the screen boundary
        if self.xcor() >= -500 + self.shapesize()[1] * 10:
            new_x = self.xcor() - self.move_distance
            self.goto(new_x, self.ycor())

    def go_right(self):
        # limit the paddle movement within the screen boundary
        if self.xcor() <= 500 - self.shapesize()[1] * 10:
            new_x = self.xcor() + self.move_distance
            self.goto(new_x, self.ycor())

    def shrink(self):
        if self.shapesize()[1] > 10:
            self.shapesize(1, 6)
