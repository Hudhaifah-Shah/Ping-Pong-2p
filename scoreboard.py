#!/usr/bin/env python3
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(x_cor, 195)
        self.show_score()
    def show_score(self):
        self.write(self.score, font=("Arial", 30, "normal"))
    def increment_score(self):
        self.clear()
        self.score += 1
        self.show_score()
