from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00ff00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
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

class Food:
    def __init__(self):
        # placing the food object randomly
        # defining 14 possible spots in the x and y exes, picking one of the spots randomly
        # -1 makes it exclusive, * space size converts it to pixels
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        # setting the coordinates
        self.coordinates = [x,y]

        # drawing food object on the canvas
        # setting color and a tag to make it easier to delete the object
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake Game LS")
window.resizable(False, False)

score = 0
direction = 'down'
# setting up the window
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# creating the game board
canvas = Canvas(window, background=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# window centralization
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# adjust the position of the window
# casting the values to integer, so they can be used it in the geometry
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

# setting the geometry
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


snake = Snake()
food = Food()

window.mainloop()