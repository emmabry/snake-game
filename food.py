from turtle import Turtle
import random as r

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.change_position()
        
    def change_position(self):
        x_axis = r.randint(-280, 280)
        y_axis = r.randint(-280, 280)
        self.goto(x_axis, y_axis)
        