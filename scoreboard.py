from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.goto(0, 270)
        self.update(self.score)
        self.hideturtle()
        
    def update(self, score):
        self.clear()
        self.write(f'Score: {score}', False, 'center', ('Arial', 12, 'normal'))
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'Game Over!', False, 'center', ('Arial', 12, 'normal'))