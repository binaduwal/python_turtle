from turtle import Screen
from player import Player
from car_creater import CarCreater
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(600,600)
screen.tracer(0)
player_1=Player((-100,-280))
cars=CarCreater()
scoreboard=ScoreBoard()
screen.listen()
screen.onkey(player_1.move_up,"Up")
screen.onkey(player_1.move_right,"Right")
screen.onkey(player_1.up,"Up")
screen.onkey(player_1.move_left,"Left")

screen.bgcolor("yellow")

while True:
    time.sleep(0.1)
    cars.create_cars()
    cars.move()
    for car in cars.all_cars:
        if player_1.distance(car)<20:
            player_1.restart()

    if player_1.ycor()>230:
        scoreboard.increase_1()
        player_1.restart()

    screen.update()
screen.exitonclick()
