from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.ball_speed=0.1

    def move(self):
        x_cord=self.xcor() + self.xmove
        y_cord=self.ycor() + self.ymove
        self.goto(x_cord, y_cord)

    def bounce_y(self):
        self.ymove *=-1

    def bounce_x(self):
        self.xmove *=-1
        self.ball_speed *=0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed=0.1