from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.setup(height=600, width=800)

screen.bgcolor("black")
screen.title("Damilare's Pong Game")
screen.tracer(0)


screen.listen()

screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update() 
    ball.move()

    if ball.ycor()<-280 or ball.ycor()>280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    if ball.xcor()>390:
        ball.reset_position()
        scoreboard.update_left_score()

    if ball.xcor()<-390:
        ball.reset_position()
        scoreboard.update_right_score()
        
screen.exitonclick()