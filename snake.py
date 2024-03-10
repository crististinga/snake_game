from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SQUARE_WIDTH = 20
SQUARE_HEIGHT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():


    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())


    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].xcor(), self.body[i - 1].ycor())
        self.head.forward(SQUARE_WIDTH)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)


    def reset(self):
        self.goto(0, 0)

