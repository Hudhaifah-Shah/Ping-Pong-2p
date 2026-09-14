#!/usr/bin/env python3
from turtle import Turtle
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.shapesize(0.4, 2)
        self.pu()
        self.sety(-250)
        self.setheading(90)
        self.draw_border()
    def draw_border(self):
        while self.ycor() < 250:
            self.stamp()
            self.forward(70)
