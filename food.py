from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

    def randomize(self, snake):
        x_cor = random.randint(-14, 14) * 20
        y_cor = random.randint(-14, 14) * 20
        self.goto(x_cor, y_cor)
        for i in snake.snake:
            if self.distance(i) < 10:
                self.randomize(snake)
