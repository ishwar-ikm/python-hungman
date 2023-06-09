import turtle

# Creating a Snake class for snake body and to define the behaviour of the snake
class Snake:
    body = [] # Attribute that contains turtle objects which makes the body of the snake

    # Defining a constructor to make the initial body of the snake
    def __init__(self):
        self.body = []
        self.head = turtle.Turtle() # Define the head of the snake
        self.create_snake()

    def create_snake(self):
        x = 0
        pos = (x, 0)
        for i in range(3):
            self.add_tail(pos)
            x -= 20
        self.head = self.body[0]

    # The method to add tail
    def add_tail(self, position):
        tail = turtle.Turtle(shape="square")
        tail.color("white")
        tail.up()
        tail.goto(position)
        self.body.append(tail)

    # Method to extend the tail
    def extend(self):
        self.add_tail(self.body[-1].position())

    # Method to move the snake by following the head
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].pos())
        self.head.forward(20)

    # Creating methods for the movement of head according to the input
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    # Method to reset the snake position to start the game again
    def reset(self):
        for part in self.body:
            part.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
