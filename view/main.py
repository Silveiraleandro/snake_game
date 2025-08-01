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
    pass

class Food:
    pass

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

window.mainloop()