from ball import Ball
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard
import time
from turtle import Screen


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=paddle.go_left, key="Right")
screen.onkey(fun=paddle.go_rigth, key="Left")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with right and left walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.x_bounce()

    # Detect collision with upper wall
    if ball.ycor() > 280:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -240:
        ball.y_bounce()

    # Detect colliison with bricks
    for brick in bricks.wall:
        if ball.distance(brick) < 10:
            ball.y_bounce()
            bricks.wall.remove(brick)
            brick.reset()
            scoreboard.score += 1
            scoreboard.update_scoreboard()

    # Detect when paddle misses
    if ball.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()