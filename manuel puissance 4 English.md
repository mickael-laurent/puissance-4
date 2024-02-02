1:Installation

Have an IDE of your choice
Install the required pygame,nympy dependencies using python commands on your IDE
Open the main.py file and execute it if everything goes well you should have a window which opens with the main menu

2 how to play
once the program is open you will arrive at the level selection menu
select a level and start confronting your opponent
if you win or lose you return to the level selection menu
it's your turn to play

3 technology use

language: Python 3.11
library use: Pygame-ce, nympy

4 Rules of the game

The aim of the game is to line up a series of 4 pawns of the same color on a grid with 6 rows and 7 columns. Each player has 21 pawns of one color (by convention, generally yellow or red). In turn, the two players place a pawn in the column of their choice, the pawn then slides to the lowest possible position in said column after which it is up to the opponent to play. The winner is the player who first achieves a consecutive alignment (horizontal, vertical or diagonal) of at least four pawns of his color. If, while all the squares on the game grid are filled, neither player has made such an alignment, the game is declared void.