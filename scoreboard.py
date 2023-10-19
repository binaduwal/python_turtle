from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.player_1=0
        self.update()
        self.increase_1


    def update(self):
        self.penup()
        self.goto(-250,250)
        self.write(f"player 1:{self.player_1}",align="left",font=("Courier",20,"normal"))

    def increase_1(self):
        self.player_1+=1
        self.update()

