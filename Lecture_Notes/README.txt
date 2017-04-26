1. Importing a board:

  Import a .txt file to set up the board
  Write GRID START one line before the grid starts and GRID END on the line after the grid
  Make sure to include spaces between 'o' and 'x'

  Designate the number of blocks and type as follows:
  [Type] [Number of blocks]

2. Designating Blocks:
  Types are designated by letters A,B,C:
    A = Reflecting block (only reflects the laser)
    B = Opaque block (absorbs the laser)
    C = See-through block (reflects and absorbs the laser)

  We assume that all blocks can move into allowed spaces. In the actual lazors game, there are "fixed blocks" which cannot be moved. There is no way to designate this type of block in this game.

3. Designating Lasers
  Lasers should be designated in the following format (starting the line with L). Multiple laser will require multiple lines starting with L. Note that
    L [origin x-coord] [origin y-coord] [x-direction] [y-direction]

4. Designating Points
  Points should be designated with the following format (starting the line with P)
