from turtle import Turtle


DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        for i in range(0, 41, 20):
            self.add((-1 * i, 0))
        self.head = self.snake[0]

    def grow(self):
        self.add(self.snake[-1].pos())

    def add(self, position):
        sq = Turtle("square")
        sq.penup()
        sq.goto(position)
        sq.color("purple")
        self.snake.append(sq)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x_cor = self.snake[i-1].xcor()
            y_cor = self.snake[i-1].ycor()
            self.snake[i].goto(x_cor, y_cor)
        self.head.forward(DISTANCE)

    def check(self):
        for seg in self.snake[1:]:
            if self.head.distance(seg) < 10:
                return False
        if abs(self.head.xcor()) > 290 or abs(self.head.ycor()) > 290:
            return False
        return True

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def eat(self, food):
        if self.head.distance(food) < 10:
            return True
        return False


