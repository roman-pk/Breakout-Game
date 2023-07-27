from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        # track total hits and specific colors
        self.hits = 0
        self.orange_hits = 0
        self.red_hits = 0
        self.x_move = 2
        self.y_move = 2
        # Move variable will be used to pause movement between turns
        self.moving = False

    def move(self):
        if self.moving == True:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def turn_on_movement(self):
        self.moving = True

    def go_left(self):
        if not self.moving:
            distance = 35
            new_x = self.xcor() - distance
            self.goto(new_x, self.ycor())

    def bounce_x(self):
        self.x_move *= -1  # this is reversing the direction

    def bounce_y(self):
        self.y_move *= -1  # this is reversing the direction

    def reset_position(self, paddle_x, paddle_y):
        self.goto(paddle_x, paddle_y)
        self.y_move = abs(self.y_move)
        self.moving = False

    def speed_increase(self):
        speed = 0.2
        if self.x_move < 0:
            self.x_move -= speed
        else:
            self.x_move += speed
        if self.y_move < 0:
            self.y_move -= speed
        else:
            self.y_move += speed

    def detect_hits(self, block_color):
        self.hits += 1

        # Increase speed after 4 and 8 hits
        if self.hits == 4:
            self.speed_increase()

        elif self.hits == 8:
            self.speed_increase()

        # Increase speed after collision with orange and red bricks
        if self.orange_hits == 0 and block_color == 'Orange':
            self.speed_increase()
        elif self.red_hits == 0 and block_color == 'Red':
            self.speed_increase()
