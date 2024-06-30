# Pong Game Implementation Using Pygame

## Overview

This repository contains a simple implementation of the classic game Pong using Python and the Pygame library. Pong is a two-dimensional sports game that simulates table tennis, where players use paddles to hit a ball back and forth across a court divided by a net.

## Setup Guide for Pong Game

### Prerequisites
Before you begin, make sure you have the following installed on your machine:
- [Git](https://git-scm.com/downloads) for version control.
- [Python](https://www.python.org/downloads/) (version 3.6 or higher).
- [pip](https://pip.pypa.io/en/stable/installation/) for managing Python packages.

### Step 1: Fork the Repository
1. Go to the GitHub repository page.
2. Click on the "Fork" button at the top-right corner of the page.
3. Select your GitHub account and click "Fork".

### Step 2: Clone the Repository Locally
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to store the project.
3. Run the following command, replacing `<your-forked-repo-url>` with the URL of your forked repository:
```sh
git clone <your-forked-repo-url>
```
### Step 3: Create a Virtual Environment
1. Navigate into the project directory:
```sh
cd pong-game
```
2. Create a virtual environment:
```sh
python -m venv venv
```
This creates a new virtual environment named `venv`.

### Step 4: Activate the Virtual Environment
1. On Windows, activate the virtual environment:
```cmd
venv\Scripts\activate
```
2. On macOS/Linux, activate the virtual environment:
```bash
source venv/bin/activate
```
## Step 5: Install Dependencies
1. With the virtual environment activated, install the project dependencies:
```sh
pip install -r requirements.txt
```
## Step 6: Run the Game
1. Run the main Python script to start the game:
```sh
python src/main.py
```
## Troubleshooting
If you encounter any issues during setup, ensure that you are running the commands inside the virtual environment and that your Python and pip versions are up to date.

## Additional Resources
For more information about using virtual environments, refer to the official Python documentation on [virtual environments](https://docs.python.org/3/tutorial/venv.html).


## Concepts and Logic Breakdown

### Game Objects

1. **Ball**: A circular object that moves around the screen, bouncing off the walls and paddles. 
   - Position (`x`, `y`): Center of the ball on the screen.
   - Radius: Size of the ball.
   - Velocity (`speed_x`, `speed_y`): Speed and direction of movement.

2. **Paddles**: Rectangular objects controlled by the players to deflect the ball.
   - Position (`x`, `y`): Top-left corner of the paddle.
   - Dimensions (`width`, `height`): Size of the paddle.
   - Speed: Rate at which the paddle can move up or down.

### Game Logic

1. **Movement**:
   - **Ball Movement**: The ball's position is updated by adding its velocity to its current position.
   - **Bounce**: If the ball hits the top, bottom, left, or right wall, its vertical or horizontal velocity is reversed.
   - **Collision Detection**: If the ball hits a paddle, its horizontal velocity is reversed.

2. **User Input**:
   - Player controls the left paddle using the 'W' and 'S' keys.
   - AI controls the right paddle in this basic version (could be replaced with player input for a two-player game).

3. **Scoring**:
   - Not implemented in this basic version, but could be added by checking if the ball goes past a paddle and awarding points accordingly.

4. **Game State Management**:
   - Starts with the ball centered on the screen and moving randomly.
   - Ends when a predetermined score is reached (not included in this version).

### System Design

1. **Modular Design**:
   - Separate classes for `Ball` and `Paddle`.
   - Encapsulation of movement logic within each class.

2. **Event Handling**:
   - Pygame's event queue is used to detect keyboard inputs and update paddle positions accordingly.

3. **Graphics and Drawing**:
   - Pygame's drawing functions (`draw.circle` and `draw.rect`) are used to render game objects on the screen.

4. **Performance Optimization**:
   - Simple collision detection algorithms for efficiency.
   - Fixed frame rate (60 FPS) to ensure smooth gameplay.

## Running the Game

1. Ensure you have Python and Pygame installed.
2. Clone this repository.
3. Run the game file using Python.

## Future Enhancements

- Implement scoring and game over conditions.
- Add AI opponents with varying difficulty levels.
- Improve graphics and sound effects.
- Add multiplayer functionality for networked games.

## Conclusion

This Pong game serves as a foundational example of game development using Pygame. It demonstrates object-oriented design, event handling, and graphical rendering in a practical context. The simplicity of the game makes it an excellent starting point for learning game development concepts.
