from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 800

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_x = -380
        self.starting_y = 100
        self.colors = ["red", "blue", "white", "orange", "green", "purple", "gray"]
        self.wall = []
        self.create_wall()


    def add_brick(self, position_x, position_y):
        brick = Turtle(shape="square")
        brick.color(random.choice(self.colors))
        brick.penup()
        self.wall.append(brick)
        brick.goto(position_x, position_y)

    def create_wall(self):
        # For each column
        for _ in range(5):
            # For each row
            for _ in range(31):
                self.add_brick(self.starting_x, self.starting_y)
                self.starting_x += 25
            self.starting_x = -380
            self.starting_y += 25


    def delete_brick(self, brick):
        brick.clear()

