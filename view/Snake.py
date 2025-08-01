from view.Constants import BODY_PARTS, SPACE_SIZE, SNAKE_COLOR


class Snake:
    def __init__(self, canvas):
        # setting body size and coordinates
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        # creating the list of coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        # creating squares
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)