# Battleship Madness
Battleship Madness is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.
It is a single player-based game in which the player can select the number of ships they wish to sink and the number of turns the player wants to have. The player has x number of turns (selected by the player) to sink all the ships before the game ends and the player either wins (hits all the ships) or loses.

image.png

# How to play.
Battleship Madness is based on the classic pen-and-paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).
In this version, the player enters a username of their choice (based on certain parameters) and will be given the option to select the number of ships (Between 1-10 inclusive) the player wishes to sink and then provided with a second option in regards the number of turns the player wishes to have (Between 1-20 inclusive).
Then a board will appear with columns A-G and rows 1-6. The number of ships that the player chose will appear randomly on the board (The player will not see where on the board the ships will appear).
The player will then guess where the ships are on the board by selecting a row (1-6) and column (A-G).
The Player will win, if they manage to sink all the ships on the board and will lose if they run out of turns before they sink all the ships.
Ships are denoted as ‘X’ and misses are denoted as ’-‘.



# Features
## Existing Features
- Random board generation:
 - The ships are randomly placed on the board.
 - There is a Hidden board (Which the ships are placed on and are hidden from the player) and Guess Pattern board (Which is the board that provides the player with all their guesses (Hits and Misses) once selected by the user and is shown to the player).

- Accepts user input:
  - Player can select the number of ships to be placed on the board (Between 1-10 inclusive).
  - Player can select the number of turns they wish to have (Between 1-20 inclusive).
  - Player must enter a username.
  - Enter in a row choice (1-6 inclusive)
  - Enter in a column choice (A-G inclusive).

- Input validation and error checking:
  - Player cannot enter coordinates outside the size of the board (i.e. Row number outside of 1-6 and column outside of A-G).
  - Username cannot contain numbers.
  - Username cannot contain special characters (!£$%^7@ etc.).
  - Username most be minimum 3 and maximum 6 characters long.
  - Player cannot enter the same guess previously made.


# Future Features
- Allow for a two-player game (Player v Computer).
- Allow for the player the option to reset the game once finished.

# Testing:
I have manually tested this project by doing the following:
- Passed the code through a Code Institute PEP8 linter and confirm that there are no major problems.
- Given invalid inputs: entering special characters and numbers when it should only be letters, out of bounds inputs, same input twice etc.
- Tested in my local terminal and the Code Institute Heroku terminal.

# Bugs
## Solved Bugs.
- When I wrote the code to prevent the player from entering special characters however the username was passed when letters were introduced. Now this has been corrected by stating “elif not values.isalmun()”
- When the player selects hits enter on the column selection, an error would appear. This was corrected by creating a column_select list of A-G and validating the players choice through this list.
# Remaining Bugs
- No bugs remaining.

# Validator Testing:
- PEP8:
 - No major errors were returned from the Code Institute PEP8 linter.

# Deployment
This project was deployed using Code Institute’s mock terminal for Heroku.
The steps to deploy are as follows:
1. Fork or clone this repository.
2. Create a new Heroku app.
3. Set the buildbacks to Python and NodeJS in that order.
4. Link the Heroku app to the repository.
5. Click on Deploy.

The live link can be found here:

# Credits:
1.	The code used for the username input was inspired by the CI Project: [Love Sandwiches]( https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1).
2.	The code for Game functionality and the creation of the game board was inspired by the YouTube video [How to Code Battleship in Python - Single Player Game]( https://www.youtube.com/watch?v=tF1WRCrd_HQ) by Knowledge Mavens.
3.	Wikipedia for the details of the Battleships game.
4.	Code Institute for the deployment terminal.