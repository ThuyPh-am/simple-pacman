# Simple game Pacman inspired

This is a simple Pac-Man game implemented in Python using Pygame.

## Video Demo : <URL>
## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pacman.git
    ```
2. Navigate to the project directory:
    ```sh
    cd pacman
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## How to run

To run the game, execute the following command:
```sh
python project.py
```
To test the function in the project.py, execute the following command:
```sh
python -m pytest test_project.py
```
## Description
This project is inspired by the classic Pac-Man game. However, instead of the traditional Pac-Man maze, the game environment is shaped like "CS50."  

### Gameplay
* The game includes one agent (player-controlled) and one ghost (AI-controlled) to keep the structure simple.  
* The agent's goal is to eat all the food in the maze.  
* The ghost's goal is to catch the agent.  
* The game starts with both the agent and the ghost at the beginning of the maze.  
* Win condition: The agent eats all the food.  
* Lose condition: The ghost catches the agent.  
* Upon winning or losing, the game ends, displaying "You win!" or "You lose!" in the terminal.  
  
### Implementation Details
The game is programmed using the Pygame library and follows an Object-Oriented Programming (OOP) approach. The project folder contains the following key files:  

* agent.py (Agent Class)  
Defines the player-controlled agent.  
Attributes include starting position, color, velocity, and size (hardcoded).  
The agent can move using arrow keys, but movement is constrained by:  
-The screen boundaries.  
- Walls in the maze.  
- Movement speed is determined by velocity.  
- The agent is drawn as a rectangle but can be customized to a different shape or character.  
  
* ghost.py (Ghost Class)
Defines the AI-controlled ghost.  
Attributes are hardcoded, including two movement speeds:  
- Idle movement (when far from the agent).  
- Chasing speed (when the agent is nearby).  
Methods:  
- move(): Moves randomly while ensuring the ghost remains within the screen and avoids walls.  
- chase(): Moves towards the agent by adjusting the x/y coordinates while ensuring walls are not passed.  
- hit(): Checks if the ghost and agent have collided.  
  
* env.py (Environment / Maze)  
Generates the "CS50"-shaped maze.  
The maze structure is defined using # characters.  
Key methods:  
- draw_env(): Converts # characters into wall rectangles on the screen.  
- is_blocked(): Checks if an object (agent or ghost) is colliding with a wall.  
The maze structure is static, so wall positions are stored in a set for efficient collision detection.   

* food.py (Food Class)
Generates food items at random positions at the start of the game.  
Stores food positions in food_map, a list of coordinates.  
The draw() method iterates through food_map and draws food items on the screen.  

* project.py (Main Game Loop)  
Runs the main game loop, handling:  
- Player input (agent movement).  
- Ghost behavior (chasing or moving idly).  
- Collisions (checking if the agent eats food or gets caught).  
- Win/Lose conditions.  
Key functions:  
- eating(): Removes food from food_map when the agent moves over it.  
- winning(): Ends the game when all food is eaten.  
- losing(): Ends the game when the ghost catches the agent.  
The ghost switches to chase mode if the agent is within a distance of 300 pixels.  
Possible Improvements  
- The ghost's movement logic could be improved to make its chasing behavior more strategic.  
- The food generation could be structured instead of fully random.  
  
#### References  
* Techwithtim [Pygame tutorial](https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial)
* Github copilot 