# Simple game Pacman inspired

This is a simple Pacman game implemented in Python using Pygame.
#### Video Demo : <URL>
#### Installation

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

#### Description

To run the game, execute the following command:
```sh
python project.py
```
To test the function in the project.py, execute the following command:
```sh
python -m pytest test_project.py
```

The project is insipired by the pacman game. The maze is replaced by the "CS50" instead of traditional pacman maze.
The game include only 1 agent and 1 ghost to simplify the structure. 
The game start with the agent and the ghost at the begining of the maze. The ghost has the mission to catch the agent while the agent has the mission of eating all the food in the maze. 
Once the agent finishes eating all the food, the player win and once the ghost catches the agent, the player loose.
Once winning or losing, the game ends and the statement "You win!" or "You loose!" display in the terminal.

The game is progammed using pygame library. The structure of the folder contains the files agent.py, ghost.py, env.py, food.py, project.py, and test_project.py. I tried to build this program with OOP method.

The agent.py file contains the code the agent class. The starting position, color, velocity, and agent size is initiated and hard coded. The agent has only one method of moving. This method allows player to control the agent to move to the positioin of food by arrow keys on the keyboard. The moving method needs to check for three things whenever the player hit a key, which key it is to define the direction of moving the agent, the current position of agent to ensure the agent does not move out of the screen frame, and if the current position is blocked by the wall so that the agent won't move through the wall. 
The velocity of the agent decide how far the agent can move by one key pressed.
The other method is the conventional setup for pygame to draw the agent as a rectangle. This can be customized into a character or other shapes.

The ghost.py defines the class of the ghost. The set up of the ghost is hard coded. The ghost has two velocity, for chasing the agent and for moving idly. 
The ghost has three methods, moving, chasing, hit. The moving method check if the ghost is inside the screen frame and is not blocked by the wall so that it can move idly. I hard coded a few situations for the ghost to move, otherwise just reset the position of the ghost to handle edge case. The chase method to find the agent position and follow by simply increase or decrease the x coordinate or y coordiante by the velocity in chasing case meanwhile ensure that the ghost won't move through the wall!
The hit method simply comparing the position of the agent and the ghost are the same the return True. 

The env.py is to generate the "CS50" maze. The init method to initialize the "CS50" by # character. The draw_env method is to checking all the # character and draw the rectangle as the postion of # map to the screen frame. The logic and the rationale behind the grid_generator is that the game is static with only one level so it would be more efficient to remember all the position of the block of the wall as the pair of x and y in a set then look up to check if any object is hitting the wall. The method is_block check if the object collide with the wall. I used the colliderect method so that it is convenient to check if the collision occurs in all edge with only 1 simple line of code. 

The food.py program the class for food. The food is generated randomly everytime the game starts and save in a food_map list. Then the draw method iterate through the list and draw rectangle at every position in the list. 

The project.py is the main function to start the game. I include 3 other functions here: eating, wining, losing. The eating function to define once the agent to move the area near the food position, that circle of food disapear from the food_map list and the screen, to animate that the agent "eat" the food. 
The wining happens when all food disapear by checking the length of the food_map. The loosing compares the position of the agent and the ghost, if they overlap then return True. 
In the main function, the loop to keep the game running. Pygame keeps redrawing every frame until winning or losing or quitting. It also contains the logic: if the distance is smaller than 300, the ghost chases the agent, else the ghost just move idly and while chase, if the ghost catches the agent, the game will end and print a statement. The loop also keeps checking if the agent win, the game will end and print a statement "You win!"

The logic behind the ghost is not detailed enough for the ghost to make sophisticated moves and the food could have also been generated in a more structure way rather than random. 

