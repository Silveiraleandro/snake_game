from tkinter import *
import random
from view.Food import Food
from view.Snake import Snake
from view.Constants import BACKGROUND_COLOR, GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE, SNAKE_COLOR, SPEED


class Game:
    def __init__(self):
        self.score = 0
        self.direction = 'down'

        self.window = Tk()
        self.window.title("Snake Game LS")
        self.window.resizable(False, False)

        self.label = Label(self.window, text="Score: 0", font=('consolas', 40))
        self.label.pack()

        self.canvas = Canvas(self.window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
        self.canvas.pack()

        self.center_window()

        self.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.change_direction('down'))

        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)

    def run(self):
        self.next_turn()
        self.window.mainloop()

    def center_window(self):
        self.window.update()
        x = int((self.window.winfo_screenwidth() / 2) - (self.window.winfo_width() / 2))
        y = int((self.window.winfo_screenheight() / 2) - (self.window.winfo_height() / 2))
        self.window.geometry(f"{self.window.winfo_width()}x{self.window.winfo_height()}+{x}+{y}")

    def next_turn(self):
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.snake.squares.insert(0, square)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.food = Food(self.canvas)
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(SPEED, self.next_turn)

    def change_direction(self, new_direction):
        opposites = {'left': 'right', 'right': 'left', 'up': 'down', 'down': 'up'}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def check_collisions(self):
        x, y = self.snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True
        if [x, y] in self.snake.coordinates[1:]:
            return True
        return False

    def game_over(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(
            self.canvas.winfo_width()/2,
            self.canvas.winfo_height()/2,
            font=('consolas', 70),
            text="GAME OVER",
            fill="red",
            tag="gameover"
        )
