from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import BlockManager
from scoreboard import ScoreBoard
import time

# Screen Setup
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor('Black')
screen.title('🎯🎯🎯 Breakout 🎯🎯🎯')
screen.tracer(0)

paddle = Paddle()
ball = Ball()
ball.goto(paddle.xcor(), paddle.ycor()+20)
blocks = BlockManager()
scoreboard = ScoreBoard()


def buttonclick(x,y):
    print("You clicked at this coordinate({0},{1})".format(x,y))

# Bind keys to moving the paddle left and right
screen.listen()
screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')
# Release the ball with space bar
screen.onkey(ball.turn_on_movement, 'space')
screen.onscreenclick(buttonclick)


game_on = True

while game_on:
    screen.update()
    ball.move()
    # Move ball with paddle if the ball is not flying
    if not ball.moving:
        new_x = paddle.xcor()
        ball.goto(new_x, ball.ycor())
    # Bounce from walls
    if ball.xcor() >= 490 or ball.xcor() <= -490:
        ball.bounce_x()

    if ball.ycor() >= 300:
        ball.bounce_y()
        # Shrink the paddle on the first collision with ceiling
        paddle.shrink()

    # Bounce from the paddle: evaluate y coordinates first and then distance to the paddle
    if paddle.ycor() <= ball.ycor() <= paddle.ycor() + 20:
        if ball.distance(paddle) < paddle.shapesize()[1] * 10:
            ball.y_move = abs(ball.y_move)

    # Reset when the ball misses the paddle
    if ball.ycor() <= paddle.ycor()-50:
        ball.reset_position(paddle.xcor(), paddle.ycor() + 20)
        scoreboard.lower_lives()

    # Detect collision with block
    for block in blocks.all_blocks:
        # Check if collision is from top or bottom
        if block.xcor() - 50 <= ball.xcor() <= block.xcor() + 50:
            if abs(block.ycor() - ball.ycor()) <= 30:
                blocks.break_block(block)
                ball.bounce_y()
                # Increase speed and reflect that on the scoreboard
                scoreboard.increase_speed(ball.detect_hits(block.color()[0]))
                scoreboard.increase_score(block.point)
        # Check if collision is from the sides
        elif block.ycor() - 20 <= ball.ycor() <= block.ycor() + 20:
            if abs(block.xcor() - ball.xcor()) <= 60:
                blocks.break_block(block)
                ball.bounce_x()
                # Increase speed and reflect that on the scoreboard
                scoreboard.increase_speed(ball.detect_hits(block.color()[0]))
                scoreboard.increase_score(block.point)

    # Check lives and blocks on the screen:
    if scoreboard.lives == 0:
        game_on = False
        scoreboard.game_over()
    elif len(blocks.all_blocks) == 0:
        game_on = False
        scoreboard.you_won()

screen.exitonclick()
