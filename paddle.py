from turtle import Turtle
DISTANCE=20
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1 )
        self.color("white")
        self.goto(position)

    def paddle_up(self):
        new_ycor=self.ycor() + DISTANCE
        new_xcor=self.xcor()
        self.goto(new_xcor, new_ycor)

    def paddle_down(self):
        new_ycor=self.ycor() - DISTANCE
        new_xcor=self.xcor()
        self.goto(new_xcor, new_ycor)
            
    