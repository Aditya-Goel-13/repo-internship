from flask import Flask
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score



app = Flask(__name__)


@app.route("/")
def home():
    return "hello world"


@app.route("/Snake_Game")
def snake_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    dif = screen.textinput(title="Difficulty", prompt="Choose Difficulty(Hard/Normal/Easy)").lower()

    score = Score(dif)
    snake = Snake()
    food = Food()
    food.randomize(snake)

    game = True
    t = 0.15

    screen.listen()
    screen.onkeypress(snake.up, key="w")
    screen.onkeypress(snake.down, key="s")
    screen.onkeypress(snake.left, key="a")
    screen.onkeypress(snake.right, key="d")

    while game:
        screen.update()
        time.sleep(t)
        snake.move()

        if snake.eat(food):
            if t > 0.1:
                if dif == "hard":
                    t = t - 0.015
                else:
                    t -= 0.01
            else:
                if dif == "hard":
                    t -= 0.005
                elif dif == "normal":
                    t -= 0.0025
            food.randomize(snake)
            snake.grow()
            score.inc()

        game = snake.check()

    score.over()
    screen.update()
    return "Thanks for playing"


if __name__ == "__main__":
    app.run(debug=True)
