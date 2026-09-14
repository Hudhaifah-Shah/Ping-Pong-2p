#!/usr/bin/env python3
from turtle import Turtle
from random import randint
SPEED = 20
X_EDGE = 280
Y_EDGE = 230
class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_ball(randint(-45, 45))
    def create_ball(self, direction):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.home()
        self.setheading(direction)
    def move(self):
        self.forward(20)
        self.bounce_off_walls()
        self.point = self.new_ball()
    def bounce_off_walls(self):
        if self.ycor() > Y_EDGE and 90 > self.heading() > 0:
            self.setheading(randint(290, 340))
        if self.ycor() > Y_EDGE and 180 > self.heading() > 90:
            self.setheading(randint(200, 250))
        if self.ycor() < -Y_EDGE and 360 > self.heading() > 270:
            self.setheading(randint(20, 70))
        if self.ycor() < -Y_EDGE and 270 > self.heading() > 180:
            self.setheading(randint(110, 160))
    def new_ball(self):
        if self.xcor() > X_EDGE:
            self.create_ball(randint(-45, 45))
            return "player 2"
        elif self.xcor() < -X_EDGE:
            self.create_ball(randint(135, 225))
            return "player 1"
