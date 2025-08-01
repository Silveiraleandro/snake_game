from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
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

def next_turn(snake, food):
    # unpacking the head of the snake
    x, y = snake.coordinates[0]

    # checking out directions
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    # updating the coordinates of the head of the snake
    snake.coordinates.insert(0, (x, y))

    # creating a new graph for the head of the snake
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # adds the ability to eat food to the snake if indexes overlap
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1

        label.config(text="Score:{}".format(score))

        # delete the food object using tag
        canvas.delete("food")
        # create a new object
        food = Food()

    else:
        # attempt to delete the last body part of the snake
        # only delete the last body part if the snake does not eat a food object
        del snake.coordinates[-1]
        # updating canvas
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # if there is a collision we call game over, otherwise we update to the next turn
    if check_collisions(snake):
        game_over()
    else:
        # calling the next turn
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    # unpacking the head of the snake
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    # defining gameover, setting text, centralizing it
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

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

# adding some control to the snake
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)
window.mainloop()