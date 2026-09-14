#!/usr/bin/env python3
from turtle import Turtle
TOP_EDGE = 210
BOTTOM_EDGE = -210
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle()
        self.setx(position)
        self.speed(0)
    def create_paddle(self):
        self.shape("square")
        self.shapesize(0.5, 3)
        self.setheading(90)
        self.penup()
        self.color("white")
    def up(self):
        if self.ycor() < TOP_EDGE:
            self.forward(50)
    def down(self):
        if self.ycor() > BOTTOM_EDGE:
            self.backward(50)
