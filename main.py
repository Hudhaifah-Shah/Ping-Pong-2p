#!/usr/bin/env python3
from random import randint
from turtle import Screen, done
from paddle import Paddle
from ball import Ball
from border import Border
from scoreboard import Scoreboard
from tkinter import messagebox
import time
screen = Screen()
screen.title("Pong Game")
winning_score = screen.numinput("Winning Score", "Enter the winning score")
screen.tracer(0)
screen.setup(width= 600, height= 500)
screen.bgcolor("black")
ball = Ball()
player_1 = Paddle(250)
player_2 = Paddle(-250)
boundary = Border()
score_1 = Scoreboard(40)
score_2 = Scoreboard(-60)
screen.update()
time.sleep(0.5)
screen.listen()
screen.onkey(player_1.up, "Up")
screen.onkey(player_1.down, "Down")
screen.onkey(player_2.up, "w")
screen.onkey(player_2.down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if player_1.distance(ball) < 30:
        ball.setheading(randint(135, 225))
    elif player_2.distance(ball) < 30:
        ball.setheading(randint(-45, 45))
    elif ball.point == "player 1":
        score_1.increment_score()
    elif ball.point == "player 2":
        score_2.increment_score()
    if score_1.score == winning_score:
        game_is_on = False
        messagebox.showinfo("Winner", "Player 1 is the winner!")
    elif score_2.score == winning_score:
        game_is_on = False
        messagebox.showinfo("Winner", "Player 2 is the winner!")
done()
