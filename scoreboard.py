from food import Food
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Food):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Scoreboard: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER THANG NGU",align=ALIGNMENT,font=FONT)


