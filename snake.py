from turtle import Turtle

# creating snake's body
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.snake_body.append(new_square)

    # 2. adding reset()
    def reset(self):
        # getting rid of dead snakes (sending them out of screen)
        for snake in self.snake_body:
            snake.goto(1000, 1000)
        # getting snake back to a default size
        self.snake_body.clear()
        # creating a new snake
        self.create_snake()
        self.head = self.snake_body[0]

    def extend(self):
        # adding a new segment to a snake
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


