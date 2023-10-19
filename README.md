# python_turtle
Python turtle project


## Import Modules:

The code starts by importing necessary modules from the Turtle graphics library:
Turtle: Used for creating turtle graphics objects.
colormode: Sets the color mode to use RGB values.
Screen: Provides the main game window.

## CarCreater Class:

This class is responsible for creating and managing cars in the game.
It initializes an empty list all_cars to keep track of all the cars created.
The create_cars method creates cars randomly with a 1/10 probability.
Cars are represented as squares with random colors and are initially placed at a random position on the left side of the screen.
The created cars are added to the all_cars list.
The move method moves all the created cars forward by 10 units.

## Player Class:

This class represents the player-controlled turtle.
It inherits from the Turtle class.
The turtle is initialized with a "turtle" shape, a blue color, and an initial position.
It has methods to move the turtle up, right, and left, as well as to restart the turtle's position.
The turtle moves forward 10 units in the direction it's facing when one of the movement methods is called.

## ScoreBoard Class:

This class manages the game's scoreboard.
It inherits from the Turtle class.
It keeps track of the player's score (player_1).
The update method displays the player's score on the screen.
The increase_1 method increments the player's score and updates the display.
Game Setup:

A game window is created using the Screen class. It's set to 600x600 pixels in size and configured not to automatically update the screen (hence screen.tracer(0)).
Instances of the Player, CarCreater, and ScoreBoard classes are created.
Event listeners are set up for arrow key presses to control the player's turtle.

## Main Game Loop:

The game runs in an infinite loop (while True).
The time.sleep(0.1) line controls the game's speed by introducing a small delay.
The create_cars method is called to create cars, and the move method is called to move them.
A collision check is performed for each car with the player's turtle. If a collision occurs (distance between car and player is less than 20), the player's turtle is reset to its starting position.
If the player's turtle reaches the top of the screen (y-coordinate greater than 230), the player's score is increased, and the turtle is reset.
The game screen is updated to display the changes.

## Game Exit:

The game window will close when the user clicks it, thanks to screen.exitonclick().

