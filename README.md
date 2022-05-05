:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Super Block Breaker
## CS 110 Final Project
### Spring Semester, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

[Code Goblins Final Project repl](https://replit.com/join/oyhjmlfacb-walterhoess)

[Super Block Breaker Presentation Demo](#)

### Team: Code Goblins
#### Tajrean Ahmed, Walter Hoess, Evan Liu
***

## Project Description *(Software Lead)*

Our project is a variation of a brick-breaker game. Bounce a ball around by moving left and right with a platform, until all the blocks are broken. Hitting the bottol wall will deduct a life. When life reaches 0, or when all blocks arr broken, the game ends. Your score will be shown at game-over.

***    

## User Interface Design *(Front End Specialist)*

![User Interface Design](assets/interface_1.jpg)
* A start menu, in-game interface, and game over menu for our block breaker game.
* The start menu is a simple "start" button.
* The in-game interface will consist of a player-controlled platform which bounces the block breaker ball, and the ball itself.
* The game over menu displays after no balls are left on screen, and after a delay, transitions back into the start menu.

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * pygame-menu
      * https://pygame-menu.readthedocs.io/en/4.2.8/
      * Module for designing menu components and functions for the start menu.

* Class Interface Design
![Class Diagram](assets/class_diagram_1.png)
* Classes
    * Board - A player-controlled board moving left and right at the bottom of the screen, bounces the ball
    * Ball - A bouncing ball that breaks blocks when it collides with them
    * Block - Blocks which are broken by the ball, and may drop powerups. Each broken block adds to the score.

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:

* main.py
* src
    * ball.py
    * block.py
    * board.py
    * controller.py
    * foldercontents.txt
* assets
    * ball.png
    * class_diagram_1.png
    * interface_1.jpg
    * foldercontents.txt
* etc
    * foldercontents.txt

***

## Tasks and Responsibilities *(Software Lead)*

### Software Lead - Evan Liu

The software lead was responsible for uploading files for the project, keeping track of team progress and updating progress in the README. The software lead also provided feedback (comments in code), input for the decisions made by the front end specialist and back end specialist, and contributed to code/assets where necessary. Also responsible for resolving bugs in code, and testing the program to make sure everything worked.

### Front End Specialist - Walter Hoess

The front end lead was responsible for designing the draft and final interface for the game. Primarily responsible for writing the controller, which was responsible for initial window setup and game loops. These loops managed interactions between sprites on-screen, constructed menus, and defined win-lose conditions. The controller also managed the game state based on in-game progress, and updated the screen based on changes.

### Back End Specialist - Tajrean Ahmed

The back end specialist was responsible for drawing class diagrams and creating models for objects in code. These models were designed to have functions required by the controller, such as inverting the direction of the ball once the controller detected a collision with a surface. Models were based on pygame sprites.

## Testing *(Software Lead)*

* Run code to make sure it is functioning. Go down the list of things to be tested. For controls, press each key to make sure it performs the expected action. For in-game events, allow those events to occur and make sure they match up with expected behavior. 
    * No examples. Code is nonfunctioning.

## ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run main.py     | Game window and start menu appears.|               |
|  2  | Click Start button  | Game begins, with board, blocks, and ball. |   |
|  3  | Press A         | Board moves left. | |
|  4  | Press D         | Board moves right. | |
|  5  | Let ball hit board | Ball bounces horizontally (same x speed, flipped y speed). | |
|  6  | Let ball hit block | Ball bounces horizontally (same x speed, flipped y speed). Block breaks, 1 is added to the score. | |
|  7  | Let ball hit left wall | Ball bounces vertically (flipped x speed, same y speed) | |
|  8  | Let ball hit right wall | Ball bounces vertically (flipped x speed, same y speed) | |
|  9  | Let ball hit bottom wall | Ball bounces horizontally (same x speed, flipped y speed). 1 life is deducted from the total count. | |
|  10 | Let ball hit top wall | Ball bounces horizontally (same x speed, flipped y speed). | |
|  12 | Let life reach 0 | Game over screen displays, game ends. | |
|  13 | Break all blocks | Win game screen displays with total score, game ends. | |
