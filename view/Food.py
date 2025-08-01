import random
from view.Constants import GAME_WIDTH, SPACE_SIZE, GAME_HEIGHT, FOOD_COLOR

class Food:
    def __init__(self, canvas):
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
