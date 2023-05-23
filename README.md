# Mancala

## Overview

Play Mancala against the computer in the terminal!

I've had the idea for this project for a while.  In the process of learning my first coding language (Python) I've come across a few game tutorials that I really enjoyed working through, although they seemed monumentally complicated to me at that early stage in my learning journey.  Coding the computer to make not only random game moves, but to find the best moves fascinated me, so I tucked that information away for a day when I would understand and be proficient enough with Python to implement the concept in my own work.  Now at the end of Codecademy's fantastic Intro to Programming course, I finally have the skills to do just that.

Why Mancala?  I've seen games like Rock, Paper, Scissors and Tic-Tac-Toe everywhere, and although I'm sure someone has already built Mancala with Python, I have not yet come across it.  I wanted to make sure I was making something different enough from the tutorials I had already seen or worked through to ensure that I could build, from scratch, a well functioning game that had the computer making good choices for its moves most of the time.  To give the human player a fighting chance at winning the game I implemented the 'best moves' for the computer for any available free moves and used 'random moves' otherwise (rather than have it steal all the player's stones).  I plan to in the future further build upon this project to implement different levels of difficulty for the player to choose from. 


## Running the Game
At startup the player is given the option to see the rules if they are unfamiliar with the game, with the additional option during play to call the rules by typing 'rules'. The game starts on the player's turn and switches back and forth whenever the player or computer has no more turn options.  When the game has finished the final scores are tallied and the winner is announced.

Optional Rules readout presented at initialization and can be called during play by typing 'rules'

Names:
  The player name and computer name can be changed in variables 'player' and 'computer'.
  This will update the names in both the display and play usage.

At the end of the game the final scores of both the computer and player are given, and the winner is announced.
