****IMPORTING A FILE****

1. Importing a board:

  Import a .txt file to set up the board
  Write GRID START one line before the grid starts and GRID END on the line after the grid
  Make sure to include spaces between 'o' and 'x'. 

  Designate the number of blocks and type as follows:
  [Type] [Number of blocks]

  Grid will start at the top left being 0,0 and step size is by half blocks (for input only).

2. Designating Blocks:
  Types are designated by letters A,B,C:
    A = Reflecting block (only reflects the laser)
    B = Opaque block (absorbs the laser)
    C = See-through block (reflects and absorbs the laser)

  This also allows for designating fixed blocks by putting the block type (A,B,C) in the grid (see earlier section).

3. Designating Lasers
  Lasers should be designated in the following format (starting the line with L). Multiple laser will require multiple lines starting with L.
    L [origin x-coord] [origin y-coord] [x-direction] [y-direction]

4. Designating Points
  Points should be designated with the following format (starting the line with P).

******CODE EXPLANATION/RUN-THROUGH****

1. Start running the code in terminal. The code accepts the board name as an input argument (using argv). For example, if the sample board is in the same folder as the code, you can type the following in your command line:
	python [file_name].py [sample_board]
For example, I can type: 
	python il227_Lazors.py mad_1.input
  
2. On your terminal, you should see the following:
    - If applicable, that you did not fully specified the game. (This assumes you must have at least one laser, point, and block)
    - When you are done generating all possible boards.
    - When you start playing boards (this may hang for a while if the board is big).
    - If you found a winning board, it should also display. (We assume it is always found, but this may not be so if you input incorrectly or if you have different types of blocks besides what was specified earlier).
    - When the code is done running.

3. The winning board is saved by default as “Board.txt”

Other notes:
- I have tested my code on levels MAD 1 - 5 and they show results.
- initializing the Game class requires a setup file.
