from turtle import Turtle
FONT = ("courier", 14, "normal")
ALIGN = "center"


class Score(Turtle):
    def __init__(self, dif):
        super().__init__()
        self.high = 0
        self.file_name = ""
        self.getfile(dif)
        self.i = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.write(f"Score : {self.i}    High_Score : {self.high}", align=ALIGN, font=FONT)

    def inc(self):
        self.clear()
        self.i += 1
        self.write(f"Score : {self.i}    High_Score : {self.high}", align=ALIGN, font=FONT)

    def over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=("Arial", 24, "normal"))
        if self.i > self.high:
            with open(self.file_name, mode='w') as file:
                file.write(f"{self.i}")

    def getfile(self, dif):
        if dif[0] == 'h':
            self.file_name = "hard_score.txt"
        elif dif[0] == 'n':
            self.file_name = "nor_score.txt"
        else:
            self.file_name = "easy_score.txt"
        with open(self.file_name) as file:
            self.high = int(file.read())


