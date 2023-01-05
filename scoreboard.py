from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score=0
        self.right_score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.left_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(f"{self.right_score}", align="center", font=("Courier", 80, "normal"))

    def update_left_score(self):
        self.left_score +=1
        self.update_score()
        
    
    def update_right_score(self):
        self.right_score +=1
        self.update_score()
        