🐍 Snake Game
A simple classic Snake Game built with Python and Tkinter, organized using modular code for clarity and scalability.

📦 Features
Moveable snake controlled by keyboard

Food spawns at random positions

Game over when snake hits itself or wall

Score tracking

Easily configurable constants (e.g., snake speed, grid size)

🧠 Project Structure
bash
Copiar
Editar
snake_game/
├── view/
│   ├── main.py         # Entry point of the game
│   ├── Game.py         # Game loop and canvas management
│   ├── Snake.py        # Snake logic (movement, growth, collision)
│   ├── Food.py         # Food spawning logic
│   └── constants.py    # Game configuration values (grid size, colors, etc.)
🚀 Getting Started
Prerequisites
Python 3.8 or later installed

Tkinter (usually included with Python)

Run the Game
Clone the repository:

bash
Copiar
Editar
git clone https://github.com/your-username/snake_game.git
cd snake_game
(Optional) Create a virtual environment:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
Run the game:

bash
Copiar
Editar
python view/main.py
⚙️ Configuration
You can change the game's appearance and speed by editing the constants.py file:

python
Copiar
Editar
SPACE_SIZE = 20
GAME_SPEED = 100  # Lower is faster
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
🛠️ To-Do (Optional Enhancements)
 Add pause/restart functionality

 Save high scores

 Add sound effects

 Make it mobile-friendly (e.g. Kivy or Pygame port)

🧑‍💻 Author
Leandro Silveira
Your contact or GitHub link here -> https://github.com/Silveiraleandro
